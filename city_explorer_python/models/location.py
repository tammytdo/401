from app import db

from os import environ
import json
import requests

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search_query = db.Column(db.String(256), unique=True)
    formatted_query = db.Column(db.String(256), unique=True)
    latitude = db.Column(db.Float, unique=True)
    longitude = db.Column(db.Float, unique=True)

    #add models for the rest of my api responses
    #refer to how JB initialized data and how it was added
    #everytime I add a new model or change a model, remember to migrate. but don't need to initialize






    # # able to do location actions without instantiaing a location because of the @staticmethod decorator
    # def __init__(self, search_query, info):
    #     self.search_query = search_query
    #     self.formatted_query = info['formatted_address']
    #     self.latitude = info['geometry']['location']['lat']
    #     self.longitude = info['geometry']['location']['lng']

    # def serialize(self):
    #     return vars(self)

    # #static method means you access it from the class name but it doesn't require a particular instance of it
    # @staticmethod
    # def fetch(query):
    #     api_key = environ.get('GEOCODE_API_KEY')
    #     url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={api_key}'
    #     locations = requests.get(url).json()

    #     # print(locations)

    #     #single location
    #     location = Location(query, locations['results'][0])

    #     return json.dumps(location.serialize())
