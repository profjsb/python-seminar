
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "localhost"
PORT = 8083

class Simpleserver(BaseHTTPRequestHandler):
   
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<body>Hello!</body>", "utf-8"))

myServer = HTTPServer((HOST, PORT), Simpleserver)

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()