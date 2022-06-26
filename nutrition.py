
import requests
ID="e71f9c64"
NUTRITION_KEY='6a05300384fcd29a965c4f30f215d85a'

activity=input('What activity did you do today ? \n')


parameters={
    # "query":"I ran 30 km and 30 min cycling",
    "query":activity,
    "gender":"male",
    "weight_kg":60,
    "height_cm":156,
    "age":18
}

header={
    "x-app-id":ID,
    "x-app-key":NUTRITION_KEY,
   "x-remote-user-id":"0"
}
response=requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise',headers=header,json=parameters)

data=response.json()["exercises"]


header2={
    "Authorization": "Basic c24xMDpTaGFrdGlAMTIzNA=="
}

import datetime as dt

today=dt.datetime.now()

for i in data:
    parameters2={
        "sheet1":{
        "date":today.strftime("%d/%m/%Y"),
        "time":today.strftime("%H:%M:%S"),
        "exercise":i["name"].title(),
        "duration":i["duration_min"],
        "calories":i["nf_calories"]
        }
        }

    response2=requests.post(url="https://api.sheety.co/bc0e8f21d84bdf904e75f34d685a1df4/workoutTraining/sheet1",json=parameters2,headers=header2)

    print(response2.text)


response3=requests.get(url='https://api.sheety.co/bc0e8f21d84bdf904e75f34d685a1df4/workoutTraining/sheet1',headers=header2)

print(response3.json())


import os
print(os.environ['LOCALAPPDATA'])
print(type(os.environ))
