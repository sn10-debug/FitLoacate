from ntpath import join
import requests

STOCKS_API_KEY='B28SRYQOTSXD43T5'

NEWS_API_KEY='48040634ef4c43e796cbb24367654152'
parameters1={
    'function':'TIME_SERIES_INTRADAY',
    'symbol':'AAPL',
    'interval':'60min',
    'apikey':STOCKS_API_KEY

}

parameters2=parameters1.copy()
del parameters2['interval']
parameters2['function']='TIME_SERIES_MONTHLY'
import datetime as dt
today=dt.datetime.now()

parameters3={
    'qInTitle':'Apple',
    'apikey':NEWS_API_KEY

}
data1=requests.get('https://www.alphavantage.co/query',params=parameters1)
data1=data1.json()

data2=requests.get('https://www.alphavantage.co/query',params=parameters2)
data2=data2.json()

data3=requests.get('https://newsapi.org/v2/everything',params=parameters3)
data3=data3.json()

publishers=['The Times of India','The Indian Express','Forbes','Business Insider']

articles=data3['articles']
need_articles=[i for i in articles if 'Apple' in i['title']]
# print(need_articles)

import pyperclip
pyperclip.copy(str(data3))
# print(data3)

from twilio.rest import Client
account_sid='AC2873c839ad7fbc1a23ac8287f7661afe'
account_pass='2af5d2ae0854ad6476c24cc9f78a7905'
import html

server=Client(account_sid,account_pass)
if len(need_articles)==0:
    need_articles.append(articles[0])
message=html.unescape(need_articles[0]['title']+'\n'+need_articles[0]['content'])




hours=list(data1['Time Series (60min)'].keys())
num_hours=len(hours)
data_modified={}
price_9={}
price_16={}
for i in hours:
    time=i.split(' ')[1][0:2]
    if time[0]=='0':
        time=int(time[1])
    else:
        time=int(time)
    if time==9 or time==16:
        info=data1['Time Series (60min)'][i]
        data_modified[i]=info
        if time==9:
            price_9[i]=info
        else:
            price_16[i]=info

# print(data_modified)
# print((price_9))
# print(price_16)

day_fluc={}
for (k,v) in zip(price_9,price_16):
    day_close=float(price_16[v]['4. close'])
    day_open=float(price_9[k]['1. open'])

    day_fluc[k]=(day_close-day_open)*100/day_open

inflation=day_fluc[list(day_fluc.keys())[0]]
if inflation>0:
    symbol='🔼'
else:
    symbol='🔻'

message1=server.messages.create(body=f"Stock APPL {inflation} {symbol}\n{message}",from_='+16205665499',to='+918879755640')

# print(day_fluc)







