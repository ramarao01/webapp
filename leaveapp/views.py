import os
import re
from flask import flash,session,request,render_template,redirect,url_for,g
from leaveapp import leaveapp
from .forms import RegistrationForm,LoginForm
from functools import wraps
leaveapp.secret_key = os.urandom(24)
import sqlite3

leaveapp.database = "sample3.db"
print leaveapp.database



def connect_db():
    return sqlite3.connect(leaveapp.database)


#print "connect_db",connect_db()
#print sqlite3.connect('sample.db').cursor().execute("CREATE TABLE profil(title TEXT, description TEXT)")

def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('home'))
    return wrap



@leaveapp.route("/home",methods=['GET','POST'])

def home():
    g.db = connect_db()
    cur = g.db.cursor().execute('SELECT * FROM Ram')
    profile = [dict(FirstName=row[0],SurName=row[1],EmailId=row[2],MobileNo=row[3]) for row in cur.fetchall()]
    print profile
    g.db.close()
    return render_template('home.html',title='Home',profile=profile)

@leaveapp.route("/login",methods=['GET','POST'])
def login():
    form1 = LoginForm()
    error = None
    if request.method == 'GET':
        return render_template('login.html',form1=form1)
    else:
    
        if request.method == 'POST':
            print form1.username.data,form1.password.data
            if form1.username.data != 'admin' or form1.password.data != 'admin':
                error = 'Invalid credentials please try again'
            elif form1.username.data == 'admin' and form1.password.data == 'admin':
                session['logged_in'] = True
                return redirect('/home') 
            else:
                return redirect('/login')
            return render_template('login.html',error = error,form1=form1)
    
    
@leaveapp.route('/')
def main():
    return render_template('main.html')


@leaveapp.route("/regleave",methods=['GET','POST'])
def regleave():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('regleave.html',form=form)
    print form.firstname.data
    print form.name.data
    print form.gender.data
    print form.Gender.label
    if request.method == 'POST':
        if  form.validate_on_submit():
            print form.firstname.data
            
            flash('Login success %s'%(form.name.data))

            flash('Login success %s'%(form.firstname.data))
            flash('Login success %s'%(form.gender.data))
            flash('Login success %s'%(form.Gender.data))
        
            return redirect('/login')
        return render_template('regleave.html',title='Registration',form=form)







@leaveapp.route("/profile")
def profile():
	return render_template("profile.html",title='Profile')




@leaveapp.route("/leaveform")
def leaveform():
        return render_template("leaveform.html",title='Leaveform')


@leaveapp.route("/leavestatus")
def leavestatus():
        return render_template("leavestatus.html",title='leavestatus')

@leaveapp.route("/changepassword")
def ChangePassword():
        return render_template("changepassword.html",title='Change password')


@leaveapp.route("/logout",methods=['GET','POST'])
@login_required
def Logout():
    form1 = LoginForm()
    session.pop('logged_in',None)
    print session
    return render_template("login.html",title='regleave',form1=form1)



