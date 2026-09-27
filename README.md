# 🌤 Weather App

A simple Flask web app that fetches live weather data for any city using the OpenWeatherMap API.

## Features
- Search weather by city name
- Displays temperature, feels-like temperature, condition, humidity, sunrise/sunset times
- Handles invalid city names gracefully with a friendly error page

## Tech Stack
- Python, Flask
- OpenWeatherMap API (via `requests`)
- python-dotenv for secure API key storage

## Setup

1. Clone the repo
```bash
git clone https://github.com/saeeg-zenn/weather-app.git
cd weather-app
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with:
OPENWEATHER_API_KEY=your_key_here


5. Get a free API key at https://openweathermap.org/api

6. Run the app
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## What I learned
Working with a real external API — nested JSON parsing, converting Unix timestamps into readable times, and handling failures that simply can't happen with a local database, like invalid API responses or an unreliable network connection.