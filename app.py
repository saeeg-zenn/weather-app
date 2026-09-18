from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv('OPENWEATHER_API_KEY')

city = "Mumbai"

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())
data = response.json()
city_name = data['name']
temperature = data['main']['temp']
feels_like = data['main']['feels_like']
humidity = data['main']['humidity']
description = data['weather'][0]['description']

print(f"{city_name}: {temperature}°C (feels like {feels_like}°C), {description}, humidity {humidity}%")

sunrise = data['sys']['sunrise']
print(sunrise)

from datetime import datetime

sunrise = data['sys']['sunrise']
sunrise_readable = datetime.fromtimestamp(sunrise)

print(sunrise_readable)