from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
from datetime import date
import json, re, os, argparse, sys, random

global args
global file_name
global fake_driver
global element_ids
		
def wait_for_page(driver, fake):
	#Wait for Homepage to load, try different elements
	global element_ids
	try:
		if not fake:
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, element_ids[0])))
			getSource(driver)
	except TimeoutException: 	
		if len(element_ids) > 0:
			element_ids.pop(0)
			wait_for_page(driver, fake)
		else:
			print("Can\'t retrieve page!")
			driver.quit()

def getSource(driver):
	page_source = driver.execute_script("return document.documentElement.innerHTML;").encode('ascii', 'ignore').decode('ascii')
	#Format Ids
	ids = re.search(",list:\[(.*?)\]", page_source).groups()[0]
	ids = ids.replace("\"", "")
	ids = ids.replace("-2", "")
	ids = re.sub(r'([0-9]*)-0,', r'', ids)
	#Format profiles to JSON
	users = re.search("shortProfiles:\{(.*?)\}\}", page_source).groups()[0]
	users = "{" + users + "}}"
	users = re.sub(r'(?!https\b)\b(\w+):', r'"\1":', users)

	rank(ids, users)
	driver.quit()
	fake_driver.quit()


def findUser(id, count, file):	
	fake_driver.get("https://facebook.com/" + id)
	try:
		WebDriverWait(fake_driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "h1")))
		name = fake_driver.find_element_by_tag_name("h1").text
		if len(name) > 0:
			print(str(count) + ' ' + name)
			file.write(name + ',' + str(count) + '\n')
	except NoSuchElementException:
		print("Can't find name")
	except TimeoutException:
		print("Timeout on Lookup " + str(id))

def rank(ids, users):
	file = open('./logs/' + file_name, "w");
	file.write('Name,' + date.today().strftime("%m-%d-%y") + '\n')
	count = 1
	ids = ids.split(",")
	users = json.loads(users)
	for id in ids:
		if users.get(id) is not None:
			if "Facebook User" in users.get(id)['name']:
				continue 
			print(str(count) + ' ' + users.get(id)['name'])
			file.write(users.get(id)['name'] + ',' + str(count) + '\n')
		elif args.lookup: 
			findUser(id, count, file)
		count = count + 1
		if count > args.max:
			return

def login(fake):
	global fake_driver
	if not fake:
		email = raw_input("email: ")
	else:
		email = raw_input("fake account email: ")
	password = getpass()

	driver = Chrome()
	if fake:
		fake_driver = driver
	driver.get("https://facebook.com")

	username_input = driver.find_element_by_id("email")
	username_input.clear()
	username_input.send_keys(email)

	password_input = driver.find_element_by_id("pass")
	password_input.clear()
	password_input.send_keys(password)

	try:
		submit = driver.find_element_by_id("loginbutton")
		submit.click()
		wait_for_page(driver, fake)
	except NoSuchElementException:
		submit = driver.find_element_by_id("u_0_b")
		submit.click()
		wait_for_page(driver, fake)

def init():
	if os.path.exists("./logs/" + file_name):
		print("Data Already Retrieved Today! Check logs")
		sys.exit(0)
	try:
		os.mkdir("./logs")
	except OSError:
		pass

	if args.lookup:
		login(True)
	login(False)
	

parser = argparse.ArgumentParser(description='Rank your Facebook Friends.')
parser.add_argument('--lookup', action="store_true", default=False, dest="lookup",
                   help='Lookup any users that are not available in shortProfiles. ' +  
                   'Requires a 2nd account to avoid looking up users on main account.')
parser.add_argument('-max', nargs='?', const=50, default=50, type=int,
					help="Maximum number of friends to rank. Defaults to 50.")

args = parser.parse_args()
file_name = date.today().strftime("%m-%d-%y") + '.csv'
element_ids = ["BuddylistPagelet", "pagelet_megaphone"]


init()	