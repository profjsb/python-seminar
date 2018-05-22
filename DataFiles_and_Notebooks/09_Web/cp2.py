"""
Tutorial - Passing variables

This tutorial shows you how to pass GET/POST variables to methods.
"""
import os
import cherrypy

class WelcomePage:

    @cherrypy.expose
    def index(self):
        # Ask for the user's name.
        return '''
            <form action="greetUser" method="GET">
            What is your name?
            <input type="text" name="name" />
            What is your favorite color?
            <input type="text" name="color" />
            <input type="submit" />
            </form>'''
    
    @cherrypy.expose
    def greetUser(self, name = None, color = "blue"):
        # CherryPy passes all GET and POST variables as method parameters.
        # It doesn't make a difference where the variables come from, how
        # large their contents are, and so on.
        #
        # You can define default parameter values as usual. In this
        # example, the "name" parameter defaults to None so we can check
        # if a name was actually specified.
        
        if name:
            # Greet the user!
            return "<font color='%s'>Hey %s, what's up?</font>" % (color, name)
        else:
            if name is None:
                # No name was specified
                return 'Please enter your name <a href="./">here</a>.'
            else:
                return 'No, really, enter your name <a href="./">here</a>.'
        
    def secret(self):
        return "here's my password: blah!"

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.config.update({"server.socket_port": 8083})

    cherrypy.quickstart(WelcomePage())
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(WelcomePage())