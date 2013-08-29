from flask import Flask, redirect, request, url_for

app = Flask(__name__)
app.debug = True

## we can tell our view functions what HTTP methods it
## is allowed to respond to
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "performing the log in"
    else:
    	## this is a normal GET request
        return "please log in..."

@app.route("/")
@app.route("/index.html")
def redirect_to_login():
	## 301 is an HTTP error code
	return redirect("/login",301)

#app.run()
if __name__ == "__main__":
    app.run()