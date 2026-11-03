import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
get_url = "https://api.openweathermap.org/data/2.5/weather"

user = input(f"Enter you city name: ")

api_key = os.getenv("API_KEY")
params = {
    "q": user,
    "appid": api_key,
}
try:
    response = requests.get(get_url, params= params)
    
    

    if response.status_code == 200:
        data = response.json()
        tempature = data["main"]["temp"] 
        description = data["weather"][0]["description"]
        temperature_celsius = tempature - 273.15
        print(f"Weather in {user}: {description}") 
        print(f"Tempature in {user}: {temperature_celsius:.1f} C")  
    else:
        print("Error", response.status_code)
except requests.exceptions.RequestException as e:
    print(e)