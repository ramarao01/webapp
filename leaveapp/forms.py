from flask_wtf import Form
from wtforms import StringField, BooleanField, RadioField
from wtforms.validators import DataRequired
from wtforms.fields.core import StringField
from leaveapp.models import User,Post

class RegistrationForm(Form):
    firstname = StringField('firstname', validators=[DataRequired('Please enter firstname')])
    #lastname = StringField('lastname', validators=[DataRequired()])
    #emailid = StringField('emailid', validators=[DataRequired()])
    #gender = StringField('gender', validators=[DataRequired()])
    #empid = StringField('empid', validators=[DataRequired()])
    #Take form = RegistrationForm() and we can call this label as {{ form.name.label }} and   {{ form.name }} in html pages
    

    Gender = BooleanField('Gender')
    
class LoginForm(Form):
    firstname = StringField('username', validators=[DataRequired('Please enter username')])
    password = StringField('password', validators=[DataRequired('Please enter password')])


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        user = User.query.filter_by(
            firstname=self.firstname.data).first()
  
        print user.firstname
        if user.firstname is None:
            return False
        try:
            print user.password,self.password.data
            if user.password != self.password.data:
                print user.password
                return False
            else:
                print user
                return (user)

        except Exception as e:
            print "user.password is empty",e

#    def validateposts(self):
#        posts = User.query.filter_by(
#            firstname=self.firstname.data).first()
#        posts = User.query.filter_by(
#            firstname=posts.id).first()
#        return posts





class empreg(Form):
    empfirstname = StringField('empfirstname', validators=[DataRequired('Please enter firstname')])
    empmiddlename = StringField('empmiddlename', validators=[DataRequired('Please enter firstname')])
    emplastname = StringField('emplastname', validators=[DataRequired()])
    empemail = StringField('empemail', validators=[DataRequired()])
    emppwd = StringField('emppwd', validators=[DataRequired()])
    empdateofjoining = StringField('empdateofjoining', validators=[DataRequired()])

	
