
from flask import Flask, render_template, request, url_for
app = Flask(__name__)
app.debug = True

@app.route("/test")
def hello():
	return render_template('base.html', 
		   page_title="Templates", 
		   content="hello!")

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():

    if request.method == 'POST':
	    username = request.form['name']
	    if username not in (""," ",None):
	    	#return "Hey %s, what's up?" % username
	    	return render_template('base.html', 
		   			page_title="Hey %s, what's up?" % username, 
		   			content="Hey %s, what's up?" % username)
	    else:
	    	return """We really want to know your name. Add it 
	    	          <a href='%s'>here</a>""" % url_for("welcome")
    else:
    	## this is a normal GET request
        return render_template("form.html")

if __name__ == "__main__":
    app.run()