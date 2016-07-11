from flask_wtf import Form
from wtforms import StringField, BooleanField, RadioField,validators

from wtforms.fields.core import StringField
from leaveapp.models import User,Post
from leaveapp import leaveapp,db,lm,oid

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

        user = User.query.filter_by(
            firstname=self.firstname.data).first()
        print "user from database"
       # print user.firstname,user.password
  
        if user.firstname.lower() is None:
            self.firstname.errors.append('Please enter valid Username')
            return False
        if self.password.data != user.password :
            self.password.errors.append('Please enter correct Password or request HR for new password')
            return False
        self.user = user
        return user











#    def validateposts(self):
#        posts = User.query.filter_by(
#            firstname=self.firstname.data).first()
#        posts = User.query.filter_by(
#            firstname=posts.id).first()
#        return posts





class empreg(Form):
    empfirstname = StringField('empfirstname', [validators.DataRequired('Please enter firstname')])
    empmiddlename = StringField('empmiddlename', [validators.DataRequired('Please enter middlename')])
    emplastname = StringField('emplastname', [validators.DataRequired()])
    empemail = StringField('empemail', [validators.DataRequired()])
    emppwd = StringField('emppwd', [validators.DataRequired()])
    empdateofjoining = StringField('empdateofjoining', [validators.DataRequired()])

	





class leaveform(Form):
    """docstring for leaveform"""
    
    usr = StringField('usr', [validators.DataRequired('Please enter username')])
    mgr = StringField('mgr', [validators.DataRequired('Please enter managername')])
    todate = StringField('today', [validators.DataRequired('Please enter username')])
    fromdate = StringField('usr', [validators.DataRequired('Please enter username')])
    reason = StringField('reason', [validators.DataRequired('Please enter username')])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validaterequest(self):
        rv = Form.validate(self)
        if not rv:
            return False


        leavefields = [self.usr.data,self.mgr.data,self.todate.data,self.startdate.data,self.reason.data]
        for leavefield in leavefields:
            if leavefield is None:
                return False

            
        


        user = User.query.filter_by(
            firstname=self.usr.data).first()
        print "user from database"
       # print user.firstname,user.password
  
        if user.firstname is None:
            self.usr.errors.append('Please enter valid Username')
            return False

        print self.todate.data

       

        me =Post()
        me.username = leavefileds[0]
        me.manager = leavefileds[1]
        me.todate = leavefileds[2]
        me.fromdate = leavefileds[3]
        me.Reason = leavefileds[4]
        db.session.add(me)
        db.session.commit()
        self.user = user
        return user

        