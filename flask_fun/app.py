from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def home():
    return 'fun'

@app.route('/location')
def location():
    print(request.args.get('data'))
    print(request.args.get('latitude'))

    return 'this is a location'

@app.route('/hello')
def hello():
    greeting = request.args.get('greeting')
    return f"this is a greeting {greeting}"

@app.route('/weather')
def get_weather():
    latitude = request.args.get('data[latitude]')
    longitude = request.args.get('data[longitude]')

    return 'bueno'

# https://jb-flask-hello-world.onrender.com/weather?data[formatted_query]=Barcelona, Spain&data[latitude]=41.3850639&data[longitude]=2.1734035&data[search_query]=barcelona
