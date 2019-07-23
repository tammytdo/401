from flask import Flask, jsonify, request
import requests
from models.location import Location
from models.weather import Forecast
from flask_cors import CORS
from os import environ

app = Flask(__name__)
CORS(app)

@app.route('/location')
def location():
    query = request.args.get('data')
    api_key = environ.get('GEOCODE_API_KEY')
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={api_key}'
    # https://maps.googleapis.com/maps/api/geocode/json?address=barcelona&key=API_KEY

    result = requests.get(url).json()

    formatted_query = result['results'][0]['formatted_address']
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']

    return f'{formatted_query}, {latitude}, {longitude}'

@app.route('/weather')
def weather():
    
    api_key = environ.get('WEATHER_API_KEY')
    url = f'https://api.darksky.net/forecast/{api_key}/{latitude},{longitude}'
    #https://api.darksky.net/forecast/WEATHER_API_KEY/41.3850639,2.1734035

    forecasts = requests.get(url).json()

    daily_weather = [Forecast(daily).serialize()
                for daily in forecasts['daily']['data']]

    latitude = request.args['data[latitude]']
    longitude = request.args['data[longitude]']
    
    return json.dumps(daily_weather)