WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'





import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'leaveapp.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')



# email server
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = False,
MAIL_USE_SSL = True,

MAIL_USERNAME = 'kedarasettiramarao01@gmail.com'
MAIL_PASSWORD = 'password'
ADMINS = ['kedarasettiramarao01@gmail.com']







