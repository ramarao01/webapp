from flask_wtf import Form
from wtforms import StringField, BooleanField, RadioField,validators

from wtforms.fields.core import StringField
from leaveapp.models import User,Post
from leaveapp import leaveapp,db




def unique_user(form, field):
     users = User.query.filter_by(email=field.data)
     if users and users.count() > 0:
         raise ValidationError('The email address you provided is already in use.')


class RegistrationForm(Form):
    firstname = StringField('firstname', [validators.DataRequired('Please enter firstname')])
    #lastname = StringField('lastname', validators=[DataRequired()])
    #emailid = StringField('emailid', validators=[DataRequired()])
    #gender = StringField('gender', validators=[DataRequired()])
    #empid = StringField('empid', validators=[DataRequired()])
    #Take form = RegistrationForm() and we can call this label as {{ form.name.label }} and   {{ form.name }} in html pages
    

    Gender = BooleanField('Gender')
    
class LoginForm(Form):
    firstname = StringField('Firstname', [validators.DataRequired('Please enter username'),validators.Length(min=4, max=10)])
    password = StringField('password', [validators.DataRequired('Please enter password'),validators.Length(min=4, max=10)])


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = self.get_user()
        print "user from database"
       # print user.firstname,user.password
  
        if user.firstname is None:
            self.firstname.errors.append('Please enter valid Username')
            return False
        if self.password.data != user.password :
            self.password.errors.append('Please enter correct Password or request HR for new password')
            return False
        self.user = user
        return user
    def get_user(self):
        return db.session.query(User).filter_by(firstname=self.firstname.data).first()











#    def validateposts(self):
#        posts = User.query.filter_by(
#            firstname=self.firstname.data).first()
#        posts = User.query.filter_by(
#            firstname=posts.id).first()
#        return posts
class search(Form):
    search = StringField('search', [validators.DataRequired()])



class empreg(Form):
    empfirstname = StringField('empfirstname', [validators.DataRequired('Please enter firstname')])
    empmiddlename = StringField('empmiddlename', [validators.DataRequired('Please enter middlename')])
    emplastname = StringField('emplastname', [validators.DataRequired()])
    empemail = StringField('empemail', [validators.DataRequired()])
    emppwd = StringField('emppwd', [validators.DataRequired()])
    empdateofjoining = StringField('empdateofjoining', [validators.DataRequired()])

	





class leaveform(Form):
    """docstring for leaveform"""
    
    usr = StringField('usr')
    mgr = StringField('mgr', [validators.DataRequired('Please enter Manager')])
    todate = StringField('today', [validators.DataRequired('Please enter Todate')])
    fromdate = StringField('fromdate', [validators.DataRequired('Please enter Fromdate')])
    reason = StringField('reason', [validators.DataRequired('Please enter Reason')])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validaterequest(self):



        leavefields = [self.usr.data,self.mgr.data,self.todate.data,self.fromdate.data,self.reason.data]
        for leavefield in leavefields:
            if leavefield is None:
                print "Entered1"
                return False

            
        



        print self.todate.data

       

        


        

        return leavefields

        
