import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '03b5f57049b9881b93cd9ef9b6df7bb0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


app.config.update(
MAIL_SERVER='smtp.gmail.com',
MAIL_PORT='587',
TESTING=False,
MAIL_SUPPRESS_SEND = False,
MAIL_DEBUG = True,
MAIL_USE_TLS=True,
# YOU HAVE TO SET YOU ENVIRONMENT VARIABLE TO BE YOUR EMAIL
MAIL_USERNAME=os.environ['EMAIL_USER'],
# YOU NEED TO HAVE 2 STEP-AUTH ON GOOGLE ACCOUNR, AND GET AN APP PASSSWORD AND PUT IT IN THE ENVIRONMENT VARIABLE
MAIL_PASSWORD=os.environ['EMAIL_PASS']
)

mail = Mail(app)

from flaskWeb import routes