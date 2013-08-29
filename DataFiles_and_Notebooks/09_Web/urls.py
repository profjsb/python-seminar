from flask import Flask

app = Flask(__name__)
app.debug = True

## this will route / and /hello 
## the function "hi()" is called a "view function"
@app.route("/")
@app.route('/hello')
def hi():
    return "<font color='red'>Hello!</font>"

## this will route URLs like: /user/josh 
@app.route('/user/<username>')
def show_user_profile(username):
    return 'hello, username =  %s' % username

## this will route URLs like: /post/1234
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post # = %d' % post_id

# here we show off multiple input and defaults
@app.route("/doc/<int:docid>/page/<int:pageid>")
@app.route("/doc/<int:docid>", defaults={'pageid': 10})
def show_document_pages(docid,pageid):
    return "Doc = %i  and Page = %i" % (docid,pageid)

## a different way to add URL rules
## this connects the function hi() to the url /hola
## nice thing by doing it this way is that you could see all your
## mappings in one place
app.add_url_rule('/hola', "say_hola", hi)

if __name__ == "__main__":
    app.run()