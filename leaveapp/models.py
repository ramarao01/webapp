from leaveapp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True, unique=True)
    emailid = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    def __repr__(self):
        return '<User %r>' % (self.firstname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)


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