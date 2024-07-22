from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '03b5f57049b9881b93cd9ef9b6df7bb0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\amit4\\PycharmProjects\\flaskProj\\flaskWeb\\site.db'
db = SQLAlchemy(app)

from flaskWeb import routes