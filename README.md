# facebookRanker
Rank your Facebook friends using the mysterious "InitialChatFriendsList"

## THIS SCRIPT IS AGAINST FACEBOOK TERMS OF SERVICE
Any form of bot scraping of user data is against Facebook TOS<br/>
For educational purposes only :)<br/>
<sub>please don't sue me</sub>

## How to use
1. run `python retrieveSource.py` for or `python retrieveSource.py --lookup` if you are using the old Facebook layout (Must have 2 Facebook accounts!)
2. Enter accounts as prompted
3. run `python analysis.py` to see aggregate rank data and rank changes between days. Run the script over multiple days to get a clearer picture of rank.

## Dependencies
* Python
* pip
* Webdriver for Chrome
* Selenium
* pandas

## Details
Many years of discussion have been had about the nature of <a href="https://lmgtfy.app/?q=InitialChatFriendsList">"InitialChatFriendsList"</a>. Facebook's algorithm for it is under lock and key so the public will never know. What it is speculated to be based on is all kinds of interactions - Chat, Group Chat, Wall Posts, Comments, Likes, and most importantly <b>Profile Visits</b> (This list is non-exhaustive!)<br/>
Everything in the ranking is bi-directional so if you happen to visit someone's profile alot, they will shoot up the ranks. This isn't just who stalks you :)

## Who's Stalking me?
Using `analysis.py` you'll see on a day-by-day basis how ranks change. Positive increases imply activity - if you haven't done any interaction with the person, it is possible they have viewed your profile. 

## How it works
* New Layout<br/>
Selenium is used to lookup Chat Sidebar List Rankings. Ranks are written to a CSV file with today's date in the `./logs/` folder
* Old Layout<br/>
Selenium is used to open the second Facebook account first. This account is used to lookup users not available in the shortProfiles attribute. Your main account is then loaded and the InitialFriendsChatList is retrieved along with the shortProfiles. Ranks are written to a CSV file with today's date in the `./logs/` folder by matching, in order, InitialFriendsChatList ids to the shortProfiles or looking up the user using the second account.

## Future features
* read account(s) from JSON file
* persistent User tracking via local file to reduce lookups
* scheduling