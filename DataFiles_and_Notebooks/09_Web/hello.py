import http.server

class myresponse(http.server.SimpleHTTPRequestHandler):
   def do_GET(s):
       s.wfile.write("<body>Hello!</body>".encode("UTF-8"))

httpd = http.server.HTTPServer(("localhost", 8084), myresponse)
httpd.serve_forever()