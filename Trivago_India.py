import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re
import json


f = open("Trivago.html")
soup = BeautifulSoup(f,"html.parser")

db = {}

tags = soup.find_all("a",{"class":"popularCity"})
for tag in tags:
    s = tag.text.strip()
    re = ''.join([i for i in s if not i.isdigit()])
    res = re.replace("# ","")
    link = tag['href'].replace("/Tourism-","")
    db[res]="https://www.tripadvisor.in/Attractions-" + link +"#ATTRACTION_SORT_WRAPPER"


print(db)

with open('result.json', 'w') as fp:
    json.dump(db, fp)