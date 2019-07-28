from os import environ
import json
import requests
from datetime import datetime

class Forecast:

    def __init__(self, info):
        self.forecast = info['summary']
        epoch_seconds = int(info['time'])
        self.time = datetime.utcfromtimestamp(epoch_seconds).strftime("%A %B %d, %Y")

    def serialize(self):
        return vars(self)

    @staticmethod
    def fetch(latitude, longitude):
        api_key = environ.get('WEATHER_API_KEY')
        url = f'https://api.darksky.net/forecast/{api_key}/{latitude},{longitude}'

        forecasts = requests.get(url).json

        dailies = [Forecast(daily).serialize() for daily in forecasts['daily']['data']]

        return json.dumps(dailies)
