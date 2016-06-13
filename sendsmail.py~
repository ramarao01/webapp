import os

from flask import Flask
from flask.ext.mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

USERNAME = 'kedarasettiramarao01@gmail.com'
PASSWORD = '9553491072'

app.config.update(
MAIL_SERVER = 'smtp.gmail.com',
MAIL_PORT = 465,
MAIL_USE_SSL = True,
# MAIL_USE_TSL = True,
MAIL_USERNAME = USERNAME,
MAIL_PASSWORD = PASSWORD,
MAIL_FAIL_SILENTLY=False,
DEBUG = True)


mail=Mail(app)

@app.route("/")
def index():

    msg = Message("Hello",
                  sender=USERNAME,
                  recipients=[USERNAME])
    msg.body = "This is the email body"
    mail.send(msg)
    return "Sent"

if __name__ == "__main__":
    app.run()
