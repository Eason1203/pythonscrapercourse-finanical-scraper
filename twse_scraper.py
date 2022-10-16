import requests
import json

response = requests.get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20221014&selectType=30&_=1665900731336')
print(response.json()['data'])
