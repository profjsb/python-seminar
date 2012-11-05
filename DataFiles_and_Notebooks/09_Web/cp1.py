import cherrypy
class WelcomePage:
    def greetUser(self, name = None):
        if name:
            # Greet the user!
            return "Hey %s, what's up?" % name
        else:
            return 'call me like <i>http://localhost:8080/greetUser?name=Josh</i>'
    greetUser.exposed = True

cherrypy.config.update({"server.socket_port": 8090})

cherrypy.quickstart(WelcomePage())
