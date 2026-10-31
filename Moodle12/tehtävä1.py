import requests
import json

request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        print(json_response["value"])    
except requests.exceptions.RequestException as e:
    print("Error", e)