from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World, this is Python/Flask!"

if __name__ == "__main__":
    app.run()
