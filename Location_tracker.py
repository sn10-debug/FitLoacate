COORDS_ENDPOINT='http://api.openweathermap.org/geo/1.0/direct'

parameters1={
'q':'Mumbai',
'appid':'6e80c098816fd6fcb4752e68085f7df9'
}

import requests

response=requests.get(url=COORDS_ENDPOINT,params=parameters1)
import pyperclip

pyperclip.copy(str(response))
print(response.json())
