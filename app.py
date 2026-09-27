from flask import Flask, render_template, request
from dotenv import load_dotenv
from datetime import datetime
import os
import requests

load_dotenv()

app = Flask(__name__)

api_key = os.getenv('OPENWEATHER_API_KEY')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather')
def weather():
    city = request.args.get('city')

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Check if the API actually found the city, BEFORE trying to use the data.
    if response.status_code != 200:
        error_message = data.get('message', 'City not found. Please try again.')
        return render_template('error.html', error_message=error_message, city=city)

    city_name = data['name']
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p')
    sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p')

    return render_template('weather.html',
                           city_name=city_name,
                           temperature=temperature,
                           feels_like=feels_like,
                           humidity=humidity,
                           description=description,
                           sunrise=sunrise,
                           sunset=sunset)

if __name__ == '__main__':
    app.run(debug=True)