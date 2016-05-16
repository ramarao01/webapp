from flask import Flask



leaveapp = Flask(__name__)
from leaveapp import views,models
