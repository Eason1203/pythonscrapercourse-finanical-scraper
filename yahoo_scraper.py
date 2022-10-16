import requests
from bs4 import BeautifulSoup

response = requests.get('https://tw.stock.yahoo.com/class-quote?sectorId=46&exchange=TAI')
soup = BeautifulSoup(response.text, 'lxml')
date = soup.find('time').get('datatime')
#print(date)

soup.find_all('div',{'class':''})