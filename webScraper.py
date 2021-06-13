

# if i want to develop a webscraper , then i will have to first call an http request

import requests as req
from bs4 import BeautifulSoup as bs
from requests.api import options 
instagram_profile = input("Enter an instagram account: ")

http_url = "http://www.github.com/"+instagram_profile
r = req.get(http_url)
soup = bs(r.content, "html.parser")
insta_profile_pic = soup.find("img", {"alt" : "Avatar"})["src"]

print(insta_profile_pic)













