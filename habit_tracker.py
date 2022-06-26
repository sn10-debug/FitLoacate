import json
from numpy import delete
import requests
endpoint_create_user='https://pixe.la/v1/users'

parameters1={
    "token":"abhdkdcbndjksd1038",
    "username":"sn10",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=endpoint,json=parameters1)
# print(response.text)



endpoint_graph=endpoint_create_user+f'/{parameters1["username"]}/graphs'

parameters2={
    "id":'work-done',
    "name":'Hours Worked',
    "unit":'hours',
    "type":'float',
    "color":"shibafu",
    "timezone":"Asia/Kolkata"

}


header={
    "X-USER-TOKEN":parameters1['token']
}

# We use header to authenticate because giving API key as a parameter may be leaked or stoled sometimes
# Therefore we use header
# 's' https means secure which we know and this also says that the information in encrypted 

# response2=requests.post(url=endpoint_graph,json=parameters2,headers=header)
# print(response2.text)

add_endpoint=endpoint_graph+f'/{parameters2["id"]}'
import datetime as dt
today=dt.datetime.now()
def adder(x):
    x=str(x)
    if len(x)<2:
        return str(0)+str(x)
    else:
        return x


parameters3={
# "date":''.join([str(i) for i in [today.year,adder(today.month),adder(today.day)]]),

"date":today.strftime('%Y%m%d'),
"quantity":"10.0"
}

# print(today.strftime('%Y%m%d'))

# this format is YYYYMMDD

# strftime is used to change a format of the date as we do in javascript using intl

# there are many other codes to get the date in a particular format and that we can get in internet




# response3=requests.post(url=add_endpoint,json=parameters3,headers=header)
# print(response3.text)


# We can also update the quantity on a day if we did it wrong using put method

update_endpoint=add_endpoint+f'/{today.strftime("%Y%m%d")}'

response4=requests.put(url=update_endpoint,json={"quantity":"15.0"},headers=header)

print(response4.text)


# Deleting a pixel

delete_endpoint=add_endpoint+f'/{dt.datetime(year=2022,month=1,day=20).strftime("%Y%m%d")}'

response5=requests.delete(url=delete_endpoint,headers=header)
print(response5.text)




