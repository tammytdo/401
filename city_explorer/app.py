from flask import Flask, jsonify, request
import requests
from models.location import Location
from models.weather import Forecast
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/location')
def location():
    print(request.args.get('data'))
    return Location.fetch('barcelona')

@app.route('/weather')
def weather():

    # url will pass funny looking query string like below
    # actually passes more keys/values but lat/long are the ones we need 
    # http://localhost:5000/weather?data[latitude]=41.3850639&data[longitude]=2.1734035

    latitude = request.args['data[latitude]']
    longitude = request.args['data[longitude]']

    return Forecast.fetch(latitude, longitude)