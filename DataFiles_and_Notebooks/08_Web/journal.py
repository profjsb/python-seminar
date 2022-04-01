from flask import Flask, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test1.db'
db = SQLAlchemy(app)


app.debug = True

class Entry(db.Model):
    id     = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.String(80))
    entry  = db.Column(db.Text())
    start  = db.Column(db.DateTime())

    def __init__(self, title, entry):
        self.title = title
        self.entry = entry
        self.start = datetime.datetime.utcnow()

    def __repr__(self):
        return """<h1>%s (%s)</h1><br><p>%s</p>""" % (self.title,self.start,self.entry)

@app.route('/add', methods=['GET', 'POST'])
def add_entry(db=db):

    if request.method == 'POST':
        title = request.form['title']
        entry = request.form['entry']
        newe = Entry(title,entry)
        db.session.add(newe)
        db.session.commit()
		
        return render_template("entry.html")

    else:
    	## this is a normal GET request
        return render_template("entry.html")

@app.route('/show')
def show():
   entries = Entry.query.all()
   rez = ""
   for e in entries:
   	   rez += "<hr>" + str(e)

   return rez

if __name__ == "__main__":
	db.create_all()
	app.run()
