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

    result = requests.get(url).json()
    
    formatted_query = result['results'][0]['formatted_address']
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']

    return f'{formatted_query}, {latitude}, {longitude}'

@app.route('/weather')
def weather():

    # url will pass funny looking query string like below
    # actually passes more keys/values but lat/long are the ones we need 
    # http://localhost:5000/weather?data[latitude]=41.3850639&data[longitude]=2.1734035

    latitude = request.args['data[latitude]']
    longitude = request.args['data[longitude]']

    return Forecast.fetch(latitude, longitude)