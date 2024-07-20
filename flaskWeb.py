from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello, Benyamin!!!!! FUCKKKKE</h1>"


@app.route("/about")
def about():
    return "<h1>Its a me</h1>"


if __name__ == '__main__':
    app.run(debug=True)