import BaseHTTPServer
class myresponse(BaseHTTPServer.BaseHTTPRequestHandler):
   def do_GET(s):
       s.wfile.write("<body>Hello!</body>")

httpd = BaseHTTPServer.HTTPServer(("localhost", 8082), myresponse)
httpd.serve_forever()
