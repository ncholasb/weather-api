from requests import api
from apikey import api
import requests
import json

city = "Porto Alegre"
country = "BR"

api_key = api

weather_url = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')


weather_data = weather_url.json()
temp = round(weather_data['main']['temp'])
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
