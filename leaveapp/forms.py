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
    #Take form = RegistrationForm() and we can call this label as {{ form.name.label }} and   {{ form.name }} in html pages
    

    Gender = BooleanField('Gender')
    
class LoginForm(Form):
    username = StringField('username', validators=[DataRequired('Please enter username')])
    password = StringField('password', validators=[DataRequired('Please enter password')])
    


	
