import flask
import flask_sqlalchemy
import flask_restless

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test_new.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = flask_sqlalchemy.SQLAlchemy(app)

class Member(db.Model):
        # __tablename __ = "newsletter_members"
        id = db.Column(db.Integer,primary_key=True)
        last_name = db.Column(db.String(50))
        first_name = db.Column(db.String(120))
        email = db.Column(db.String(120),unique=True)

db.create_all()

manager = flask_restless.APIManager(app,flask_sqlalchemy_db=db)

manager.create_api(Member,methods=["GET","POST"])

app.run()