# API Authnetication simply means having a unique api key to get the data1 which is not freely available just can think of premium sort of

import requests

import os
from Account import set1


# This will be creating a obstruction as first the account.py will be executing first then only this will execute from here
set1()


print(os.environ.get('hello'))

API_key='6e80c098816fd6fcb4752e68085f7df9'
parameters={'q':'Mumbai','appid':API_key}

data1=requests.get(f'http://api.openweathermap.org/data/2.5/weather',params=parameters)
data1=data1.json()
# print(data1)
coords=data1['coord']
# coords['lat']=5
# coords['lon']=79
# If API key is invalid then 401 error will occur
exlude=['minutely','daily','alerts']
data2=requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={coords["lat"]}&lon={coords["lon"]}&exclude={",".join(exlude)}&appid={API_key}')
data2=data2.json()
des=data2['current']['weather'][0]['main']
hourly_data=data2['hourly']
hourly_temp=[i['temp'] for i in hourly_data]
avg=sum(hourly_temp)/len(hourly_temp)
print(format(avg-273,'0.2f')+' C')
print(des)
import pyperclip
pyperclip.copy(str(data2))

import smtplib

from twilio.rest import Client
account_sid='AC2873c839ad7fbc1a23ac8287f7661afe'
account_pass='2af5d2ae0854ad6476c24cc9f78a7905'

server=Client(account_sid,account_pass)



def check(x):
    data_12=x[:12]
    des=[]
    take=False
    for i in data_12:
        des.append(i['weather'][0]['main'])
        if i['weather'][0]['id']<700:
            take=True
    # print(des)
    
    with smtplib.SMTP('smtp.gmail.com') as connection:
        number='+918879755640'
        company_id='atlantamodel1@gmail.com'
        password='9321513030'
        user='atlantamodel2@yahoo.com'
        connection.starttls()
        connection.login(company_id,password)
        def trial(x):
            print(x.sid)
            print(x.status)
            

        if take:
            connection.sendmail(from_addr=company_id,to_addrs=user,msg="Subject:Weather Conditions\n\n Today you will be facing rain in next 12 hours !!\n So don't forget to take the Umbrella")
            message=server.messages.create(body="Today you will be facing rain in next 12 hours !!\n So don't forget to take the Umbrella",from_='+16205665499',to=number)
            trial(message)
            
        else:
            des1=list(set(des))
            max=0
            weather:str
            for j in des1:
                nums=des.count(j)
                if nums>max:
                    max=nums
                    weather=j
            if weather=='Clear':
                connection.sendmail(from_addr=company_id,to_addrs=user,msg=f'Subject:Weather Conditions\n\n Today the weather is mostly going to be {weather}')
                message=server.messages.create(body=f"Today the weather is mostly going to be {weather}",from_='+16205665499',to=number)
                trial(message)
            elif weather=='Clouds':
                 connection.sendmail(from_addr=company_id,to_addrs=user,msg=f'Subject:Weather Conditions\n\n Today the weather is mostly going to be Cloudy')  
                 message=server.messages.create(body="Today the weather is mostly going to be Cloudy",from_='+16205665499',to=number) 
                 trial(message)


        # We can only send messages to the verified numbers manually by us



# environment variables are used to declare variables in it and it can be accessed by the program without setting the varaible in it just by importing os and this can be used for security purpose

# This we have already done in the pythonanywhere

# ';' in pythonanywhere is used to represent a new line

check(hourly_data)



