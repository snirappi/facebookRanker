# facebookRanker
Rank your Facebook friends using the mysterious "InitialChatFriendsList"

## THIS SCRIPT IS AGAINST FACEBOOK TERMS OF SERVICE
Any form of bot scraping of user data is against Facebook TOS<br/>
For educational purposes only :)<br/>
<sub>please don't sue me</sub>

## Dependencies
* Python
* pip
* Webdriver for Chrome
* Selenium

## Details
Many years of discussion have been had about the nature of <a href="https://lmgtfy.app/?q=InitialChatFriendsList">"InitialChatFriendsList"</a>. Facebook's algorithm for it is under lock and key so the public will never know. What it is speculated to be based on is all kinds of interactions - Chat, Group Chat, Wall Posts, Comments, Likes, and most importantly <b>Profile Visits</b> (This list is non-exhaustive!)<br/>
Everything in the ranking is bi-directional so if you happen to visit someone's profile alot, they will shoot up the ranks. This isn't just who stalks you :)

## Limitations
Currently, facebookRanker just pulls profile information using the given shortProfiles. Not all profile Ids in InitialChatFriendsList are represented in shortProfiles. It would be straightforward to lookup the profiles and retrieve user information <b>however</b> the act of looking users up will artificially increase weight on certain users, thereby disrupting the algorithms "natural" data.<br/>
Looking them up while not logged in could be viable however some profiles are locked from public view.
