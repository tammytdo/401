# from http.server import BaseHTTPRequestHandler, HTTPServer
# from urllib.parse import urlparse, parse_qs
# import os
# import json

# from dotenv import load_dotenv
# load_dotenv()

# from models.location import Location
# from models.weather import Forecast

# class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         parsed_path = urlparse(self.path)
#         parsed_qs = parse_qs(parsed_path.query)

#         if parsed_path.path == '/location' and parsed_qs.get('data'):
#             self.send_response(200)
#             self.send_header('Content-type', 'application/json')
#             self.end_headers()

#             location_query = parsed_qs.get('data')[0]
#             json_string = Location.fetch(location_query)
#             self.wfile.write(json_string.encode())
#             return

#         elif parsed_path.path == '/weather':
#             self.send_response(200)
#             self.send_header('Content-type', 'application/json')
#             self.end_headers()

#             #how does this work if if parsed_qs returns {}?
#             latitude = parsed_qs['data[latitude]'][0]
#             longitude = parsed_qs['data[longitude]'][0]
#             json_string = Forecast.fetch(latitude, longitude)
#             self.wfile.write(json_string.encode())
#             return latitude, longitude, json_string

#         self.send_response_only(404)
#         self.end_headers()


# def create_server():
#     return HTTPServer(
#     ('127.0.0.1', int(os.environ['PORT'])), SimpleHTTPRequestHandler
# )

# def run_forever():
#     server = create_server()

#     try:
#         print("Starting server on port {}.".format(os.environ['PORT']))
#         server.serve_forever()

#     except KeyboardInterrupt:
#         server.server_close()
#         server.shutdown()

# if __name__ == "__main__":
#     run_forever()
