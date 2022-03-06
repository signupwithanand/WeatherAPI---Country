import requests
import pandas as pd

api_key = '91efa77e72fb9e910f90fe2197248f5c'
city_name = "Chennai"
units = "metrics"

def country_weather(city,api_key = api_key,units = 'metric'):
  url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  content = r.json()
  with open("data.txt", "a+") as file:
    for item in content['list']:
      time = item['dt_txt']
      temp = item['main']['temp']
      condition = item['weather'][0]['description']
      file.write(f"{city}, {time}, {temp}, {condition}\n")
      
print(country_weather(city = "Srinagar"))

