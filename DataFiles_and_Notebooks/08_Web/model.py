from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
print(app.config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

app.debug = True

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return 'Yo, my name is %r' % self.username

    def __str__(self):
        return self.__repr__()


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    addresses = db.relationship('Address', backref='person',
                                lazy='dynamic')

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))


db.create_all()
admin = User('admin', 'admin@example.com')
guest = User('guest', 'guest@example.com')
db.session.add(admin)
db.session.add(guest)
try:
	db.session.commit()
except:
	pass

@app.route("/users")
def get_users():
   1/0
   return(" ".join([str(x) for x in User.query.all()]))
   #return repr([x.email for x in User.query.all()])

@app.route("/admin")
def get_admin_email():
   admin = User.query.filter_by(username='admin').first()
   return "<b>Admin Email</b>: %s" % admin.email

if __name__ == "__main__":
    app.run()

