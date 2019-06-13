#!/usr/Python3
import requests
from bs4 import BeautifulSoup
web=requests.get('http://192.168.10.30/adhoc.html')
# This will print status code
print(web.status_code)
# This will print original front end data(HTML)
t=web.text
print(t)
print(web.url)
soup=BeautifulSoup(t,'lxml')
print(soup.select('marquee'))
p=soup.select('marquee')
print(p[0].text)
# For printing multiple tags
tag=soup.select('p')
for i in tag:
    print(i.text)

