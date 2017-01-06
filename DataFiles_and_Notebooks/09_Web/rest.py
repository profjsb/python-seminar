import flask
import flask.ext.sqlalchemy
import flask.ext.restless

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

db = flask.ext.sqlalchemy.SQLAlchemy(app)

class Member(db.Model):
        # __tablename __ = "newsletter_members"
        id = db.Column(db.Integer,primary_key=True)
        last_name = db.Column(db.String(50))
        first_name = db.Column(db.String(120))
        email = db.Column(db.String(120),unique=True)

db.create_all()

manager = flask.ext.restless.APIManager(app,flask_sqlalchemy_db=db)

manager.create_api(Member,methods=["GET","POST"])

app.run()