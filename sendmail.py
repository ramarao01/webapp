from flask import Flask
from flask.ext.mail import Mail, Message
app = Flask(__name__)

USERNAME = 'ramarao.kedarasetti@nexiilabs.com'
PASSWORD = '9553491072'

app.config.update(
MAIL_SERVER = 'email.nexiilabs.com',
MAIL_PORT = 993,
MAIL_USE_SSL = True,
MAIL_USE_TSL = True,
MAIL_USERNAME = USERNAME,
MAIL_PASSWORD = PASSWORD,
MAIL_FAIL_SILENTLY=True,
DEBUG = True)



mail = Mail(app)


@app.route('/')
def index():
	msg = Message('Hello', sender = 'ramarao.kedarasetti@nexiilabs.com',recipients = ['manikanth.patwari@nexiilabs.com'])
	mail.send(msg)
	return 'Message sent'


if __name__  == '__main__':
	app.run(debug=True)
