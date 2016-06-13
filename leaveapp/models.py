from leaveapp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(120), index=True, unique=True)
    DateOfBirth = db.Column(db.String(120), index=True)
    MaritalStatus = db.Column(db.String(64), index=True)
    Gender = db.Column(db.String(64), index=True)
    lastname = db.Column(db.String(64), index=True)
    middlename = db.Column(db.String(64), index=True)
    firstname = db.Column(db.Integer, index=True)
    City = db.Column(db.String(64), index=True, unique=True)
    Skypeid = db.Column(db.String(64), index=True, unique=True)
    Reportingto = db.Column(db.String(64), index=True)
    empid = db.Column(db.Integer, index=True, unique=True)
    displayname = db.Column(db.String(64), index=True, unique=True)
    emailid = db.Column(db.String(64), index=True, unique=True)
    DateOfjoining = db.Column(db.String(64), index=True)
    
    Mobilenum = db.Column(db.String(64), index=True)
    BloodGroup = db.Column(db.String(64), index=True)

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