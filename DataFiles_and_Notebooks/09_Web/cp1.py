import cherrypy

PORTNUM = 8098

class WelcomePage:
    def greetUser(self, name = None):
        if name:
            # Greet the user!
            return "Hey %s, what's up?" % name
        else:
            return 'call me like <i>http://localhost:{}/greetUser?name=Josh</i>'.format(PORTNUM)
    
    greetUser.exposed = True

cherrypy.config.update({"server.socket_port": PORTNUM})

cherrypy.quickstart(WelcomePage())