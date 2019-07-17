# Features
# In index.py create the following endpoints:

# GET /locations?data=barcelona - returns a valid json response that matches structure { 'formatted_query':'the place', 'search_query':'what they typed', 'latitude':100.0, 'longitude':100.0 }
# Stretch Goals
# Make super class to encapsulate common resource functionality
# Make a static method on resource class to handle fetching the data from api

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
import json
import requests

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)

        print('request path', parsed_path.path)

        parsed_qs = parse_qs(parsed_path.query)

        print('parsed query', parsed_qs)
        
        if parsed_path.path == '/':
            print("hello code")
            self.send_response(200, "string")
            self.send_header('Content-type', 'text')
            self.end_headers()

            json_string = json.dumps("json stringy")
            self.wfile.write(json_string.encode())
            return


def create_server():
    return HTTPServer(
    ('127.0.0.1', 3000), SimpleHTTPRequestHandler
)

def run_forever():
    server = create_server()

    try: 
        print(f'Starting server on port 3000')
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        server.shutdown()

if __name__ == "__main__":
    run_forever()