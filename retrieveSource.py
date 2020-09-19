from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import json
import re

def getSource(driver):
	#Wait for Homepage to load
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "pagelet_megaphone")))
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

def rank(ids, users):
	count = 1
	ids = ids.split(",")
	users = json.loads(users)
	for id in ids:
		if users.get(id) is not None:
			print(str(count) + ' ' + users.get(id)['name'])
		count = count + 1

email = raw_input('email: ')
password = getpass()

driver = Chrome()
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
	getSource(driver)
except NoSuchElementException:
	submit = driver.find_element_by_id("u_0_b")
	submit.click()
	getSource(driver)
		
