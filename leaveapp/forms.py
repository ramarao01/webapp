from flask_wtf import Form
from wtforms import StringField, BooleanField, RadioField
from wtforms.validators import DataRequired
from wtforms.fields.core import StringField

class RegistrationForm(Form):
    firstname = StringField('firstname', validators=[DataRequired('Please enter firstname')])
    #lastname = StringField('lastname', validators=[DataRequired()])
    #emailid = StringField('emailid', validators=[DataRequired()])
    #gender = StringField('gender', validators=[DataRequired()])
    #empid = StringField('empid', validators=[DataRequired()])
    name = StringField('Name Of Student',validators=[DataRequired('Please enter your name.')])
    gender = BooleanField('Gender')
    Gender = BooleanField('gender')
class LoginForm(Form):
    username = StringField('username', validators=[DataRequired('Please enter username')])
    password = StringField('password', validators=[DataRequired('Please enter password')])
    


	
