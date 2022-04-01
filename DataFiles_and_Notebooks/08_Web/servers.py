'''
One of the benefits of the WSGI spec is that you can use any WSGI compliant
server to serve up your app. A server may have been written to support different
kinds of features:

 * speed, performance (multi-threaded, written in a compiled language like C)
 * extensibility (written in pure Python)
 * ease of development (code reloading, extra debugging features)
 * adapters for a larger server platform (e.g. mod_wsgi for Apache, or the WSGI
   adapter for Google App Engine)

Depending on what you need for development or deployment you can pick a server
that matches your needs best.

This script shows the same app running under three different servers. Run this
script and pass in the name of the server you want to use as a command line
argument. These servers are available:

 * wsgiref - the reference implementation for a WSGI server from the python
             standard library, bare bones
 * werkzeug - provides a nice server with code reloading and interactive
              over-the-web debugging, great for development!
 * cherrypy - a very performant server, good for production deployment

Also notice how the environ changes based on which server is used. Some servers
will only pass through the environment variables defined in the WSGI spec.
'''

import pprint
from wsgiref.util import setup_testing_defaults

def application(environ, start_response):
    setup_testing_defaults(environ)
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items() if key.find("wsgi") != -1]
    return ret


if __name__ == '__main__':
    import sys
    arg = sys.argv.pop(-1)

    if arg == 'wsgiref':
        from wsgiref.simple_server import make_server
        print("Serving on http://localhost:4000...")
        make_server('localhost', 4000, application).serve_forever()

    elif arg == 'werkzeug':
        from werkzeug import run_simple
        run_simple('localhost', 4000, application, use_debugger=True)

    elif arg == 'cherrypy':
        from cherrypy import wsgiserver
        server = wsgiserver.CherryPyWSGIServer(('localhost', 4000), application)
        print("Serving on http://localhost:4000...")
        try:
            server.start()
        except KeyboardInterrupt:
            print('Shutting down.')
            import sys; sys.exit();

    else:
        print('''Please provide one of:
* wsgiref
* werkzeug
* cherrypy''')
