import time
import http.server

HOST_NAME = 'localhost' #
PORT_NUMBER = 8091 # Maybe set this to 9000.

def s2b(s):
    return bytes(s, 'utf-8')

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header(s2b("Content-type"), s2b("text/html"))
        s.end_headers()

    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header(s2b("Content-type"), s2b("text/html"))
        s.end_headers()
        s.wfile.write(s2b("<html><head><title>Title goes here.</title></head>"))
        s.wfile.write(s2b("<body><p>This is a <i>test.</i></p>"))
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        s.wfile.write(s2b("<p>You accessed path: %s</p>" % s.path))
        s.wfile.write(s2b("</body></html>"))

if __name__ == '__main__':
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime()), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    httpd.serve_forever()
    #except KeyboardInterrupt:
    #    pass
    httpd.server_close()
    print(time.asctime()), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)