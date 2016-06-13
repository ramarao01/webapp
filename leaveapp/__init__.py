from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

leaveapp = Flask(__name__)
leaveapp.config.from_object('config')
db = SQLAlchemy(leaveapp)
leaveapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

lm = LoginManager()
lm.login_view = 'login'
lm.init_app(leaveapp)
oid = OpenID(leaveapp, os.path.join(basedir, 'tmp'))

from leaveapp import views,models





from flask_mail import Mail

mail = Mail(leaveapp)




