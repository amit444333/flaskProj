import os

class Config:
    # YOU HAVE TO SET YOU ENVIRONMENT VARIABLE
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT='587'
    TESTING=False
    MAIL_SUPPRESS_SEND = False
    MAIL_DEBUG = True
    MAIL_USE_TLS=True
    # YOU HAVE TO SET YOU ENVIRONMENT VARIABLE TO BE YOUR EMAIL
    MAIL_USERNAME=os.environ['EMAIL_USER']
    # YOU NEED TO HAVE 2 STEP-AUTH ON GOOGLE ACCOUNR, AND GET AN APP PASSSWORD AND PUT IT IN THE ENVIRONMENT VARIABLE
    MAIL_PASSWORD=os.environ['EMAIL_PASS']

class ConfigTest:
    # YOU HAVE TO SET YOU ENVIRONMENT VARIABLE
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT='587'
    TESTING=False
    MAIL_SUPPRESS_SEND = False
    MAIL_DEBUG = True
    MAIL_USE_TLS=True
    # YOU HAVE TO SET YOU ENVIRONMENT VARIABLE TO BE YOUR EMAIL
    MAIL_USERNAME=os.environ['EMAIL_USER']
    # YOU NEED TO HAVE 2 STEP-AUTH ON GOOGLE ACCOUNR, AND GET AN APP PASSSWORD AND PUT IT IN THE ENVIRONMENT VARIABLE
    MAIL_PASSWORD=os.environ['EMAIL_PASS']    