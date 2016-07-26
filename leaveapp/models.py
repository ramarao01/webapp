from leaveapp import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Integer, index=True)
    lastname = db.Column(db.String(64), index=True)
    middlename = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    emailid = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(120), index=True, unique=True)

    dateofbirth = db.Column(db.String(120), index=True)
    maritalstatus = db.Column(db.String(64), index=True)
    gender = db.Column(db.String(64), index=True)
    mobilenum = db.Column(db.String(64), index=True)
    bloodgroup = db.Column(db.String(64), index=True)
    age = db.Column(db.String(64), index=True)
    
    city = db.Column(db.String(64), index=True, unique=True)
    skypeid = db.Column(db.String(64), index=True, unique=True)
    reportingto = db.Column(db.String(64), index=True)

    empid = db.Column(db.Integer, index=True, unique=True)
    dateofjoining = db.Column(db.String(64), index=True)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    def __repr__(self):
        return '<User %r>' % (self.firstname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    usedleaves = db.Column(db.Integer)
    Availableleaves = db.Column(db.Integer)
    fromdate = db.Column(db.String(140))
    todate = db.Column(db.String(140))
    Reason = db.Column(db.String(140))
    leavetype = db.Column(db.String(140))
    Applydate = db.Column(db.String(140))
    username = db.Column(db.String(140))
    noofdays = db.Column(db.String(140))
    manager = db.Column(db.String(140))

    #timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    leavestatus = db.Column(db.String(140))

    def __repr__(self):
        return '<Post %r>' % (self.id)


class Calendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.String(120))
    Month = db.Column(db.String(120))
    Week = db.Column(db.String(120))
    Holiday = db.Column(db.String(120))

class Birthday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.String(120))
    Month = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.firstname'))
    


@property
def is_authenticated(self):
        return True

@property
def is_active(self):
        return True

@property
def is_anonymous(self):
        return False

def get_id(self):
    try:
    	return unicode(self.id)  # python 2
    except NameError:
        return str(self.id)  # python 3
