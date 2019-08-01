from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import json
import requests

# Python package that searches for a .env. If found, will expose the variables in it to the app. 
# from dotenv import load_dotenv
# load_dotenv()
 
PORT = 3000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        print('request path', parsed_path.path)

        parsed_qs = parse_qs(parsed_path.query)
        print('parsed query', parsed_qs)
        
        if parsed_path.path == '/locations':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            query = parsed_qs['search_query'] 
            
            url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={GOOGLE_API_KEY}'
            print('The URL is ', url)

            #get it back as json
            result = requests.get(url).json()
            
            self.formatted_query = result['results'][0]['formatted_address']
            self.latitude = result['results'][0]['geometry']['location']['lat']
            self.longitude = result['results'][0]['geometry']['location']['lng']

            json_string = json.dumps(result)
            self.wfile.write(json_string.encode())
            return

        self.send_response_only(404)
        self.end_headers()

def create_server():
    return HTTPServer(
    ('127.0.0.1', PORT), SimpleHTTPRequestHandler
)

def run_forever():
    server = create_server()

    try: 
        print(f'Starting server on PORT {PORT}')
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        server.shutdown()
        print('Ended server.')

if __name__ == "__main__":
    run_forever()

