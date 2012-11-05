"""
Tutorial - Passing variables

This tutorial shows you how to pass GET/POST variables to methods.
"""

import cherrypy


class WelcomePage:

    def index(self):
        # Ask for the user's name.
        return '''
            <form action="greetUser" method="GET">
            <p>What is your name?</p>
            <input type="text" name="name" />
            <p>And, what's your most favorite color?</p>
            <input type="text" name="color" />
            <input type="submit" />
            </form>'''
    index.exposed = True
    
    def greetUser(self, name = None, color = None):
        # CherryPy passes all GET and POST variables as method parameters.
        # It doesn't make a difference where the variables come from, how
        # large their contents are, and so on.
        #
        # You can define default parameter values as usual. In this
        # example, the "name" parameter defaults to None so we can check
        # if a name was actually specified.
        
        if name and color:
            # Greet the user!
            
            return """<FONT COLOR="%s">Hey %s, what's up?</FONT>""" % (color, name)
            
            # return "Hey %s, what's up? %s" % (name, color)
        else:
            if name is None or color is None:
                # No name was specified
                return 'Please enter your name/color <a href="./">here</a>.'
            else:
                return 'No, really, enter your name/color <a href="./">here</a>.'
    greetUser.exposed = True


import os.path
tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(WelcomePage())
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(WelcomePage())
