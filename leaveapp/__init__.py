from flask import Flask
from flask_sqlalchemy import SQLAlchemy

leaveapp = Flask(__name__)
leaveapp.config.from_object('config')
db = SQLAlchemy(leaveapp)
leaveapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True





from leaveapp import views,models





from flask_mail import Mail

mail = Mail(leaveapp)




