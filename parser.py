import requests
from bs4 import BeautifulSoup


headers = {
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding' : 'gzip, deflate, br',
'Accept-language' : 'ru,en-US;q=0.9,en;q=0.8',
'Cache-Control' : 'no-cache',
'Cookie': 'refreg=https%3A%2F%2Fotzovik.com%2Freviews%2Fbukmekerskaya_kontora_liga_stavok%2F; ssid=162305530; ownerid=01d2ff67f1a6d0a1c066049ad2aad4; referal=1; ROBINBOBIN=e352db6dlh3da2484vsl84gtc3',
'Pragma' : 'no-cache',
'Upgrade-Insecure-Requests': '1',
'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

session = requests.session()

req = session.get('https://otzovik.com/reviews/bukmekerskaya_kontora_liga_stavok/', headers=headers)
soup = BeautifulSoup(req.content, 'html.parser')

with open('test.txt', 'w') as f:
    f.write(soup.prettify())
