from flask import Flask, redirect, request, url_for

app = Flask(__name__)
app.debug = True

## we can tell our view functions what HTTP methods it
## is allowed to respond to
@app.route('/welcome', methods=['GET', 'POST'])
def welcomehi():

    if request.method == 'POST':
	    username = request.form['name']
	    if username not in (""," ",None):
	    	return "Hey %s, what's up?" % username
	    else:
	    	return """We really want to know your name. Add it 
	    	          <a href='%s'>here</a>""" % url_for("welcomehi")
    else:
    	## this is a normal GET request
        return '''
            <form action="welcome" method="POST">
            What is your name?
            <input type="text" name="name" />
            <input type="submit" />
            </form>'''

@app.route("/")
def redirect_to_login():
	## 301 is an HTTP error code
	return redirect(url_for("welcomehi"),301)

if __name__ == "__main__":
    app.run()