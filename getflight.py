

import pandas
import pyperclip
import requests

API_KEY='bCNnzeEa3HgGea-YtFU1MpZcRiB4ULY8'
endpoint_IATA='https://tequila-api.kiwi.com/locations/query'
header=  {  
    'apikey':'bCNnzeEa3HgGea-YtFU1MpZcRiB4ULY8'

}

def code_search(city):
    parameters={
        'location_types' :"city",
        'term':city
    }

    response=requests.get(url=endpoint_IATA,headers=header,params=parameters)

    data=response.json()
    return data['locations'][0]['code']



from pprint import pp, pprint
from_code=code_search('London')
pprint(from_code)

flight_search_endpoint='https://tequila-api.kiwi.com/v2/search?'
file_name='Flight Deals - prices.csv'

info={
        'City':[],
        'IATA Code':[],
        'Lowest Price':[]
    }

def location_code():
    global info
    import pandas
    data=pandas.read_csv(file_name)
    
    for (_,row) in data.iterrows():
        info['City'].append(row.City)
        info['IATA Code'].append(code_search(row.City))
        info['Lowest Price'].append(row['Lowest Price'])


    pprint(info)

    data4=pandas.DataFrame(info)
    data4.to_csv('Location_details.csv',index=False)

import datetime as dt
today=dt.datetime.now()



# pprint(response2.json())


from twilio.rest import Client
account_sid='AC2873c839ad7fbc1a23ac8287f7661afe'
account_pass='2af5d2ae0854ad6476c24cc9f78a7905'

server=Client(account_sid,account_pass)



def checker(city_code,low_price):
    parameter1={
        "fly_from":from_code,
        "fly_to":city_code,
        "date_from":today.strftime('%d/%m/%Y'),
        "date_to":(today+dt.timedelta(days=6*30)).strftime('%d/%m/%Y'),
        "nights_in_dst_from":7,
        "nights_in_dst_to":28,
        "flight_type":"round"

    }

    response2=requests.get(url=flight_search_endpoint,headers=header,params=parameter1)
    pyperclip.copy(str(response2.text))
    details=response2.json()
    
    prices={i['price']:i for i in details['data']}
    # print(prices)
    for j in prices:
        if j<=low_price:
            flight=prices[j]
            message=server.messages.create(body=f"Low Price Alert ! Only at £{j} fly from {flight['cityFrom']}-{flight['flyFrom']} to {flight['cityTo']}-{flight['flyTo']} ",from_='+16205665499',to='+918879755640')
            print(message.status)
            break

# checker('BOM',200)

data=pandas.read_csv('Location_details.csv')



for (_,row) in data.iterrows():
    checker(row['IATA Code'],int(row['Lowest Price']))


