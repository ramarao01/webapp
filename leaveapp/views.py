import os
import re
from flask_mail import Mail, Message
from flask import flash,session,request,render_template,redirect,url_for,g,jsonify
from leaveapp import leaveapp,db,lm,oid
from .forms import RegistrationForm,LoginForm,empreg,leaveform
from functools import wraps
from .models import User,Post
leaveapp.secret_key = os.urandom(24)
import sqlite3
from sqlalchemy import and_,insert
from datetime import datetime

from flask_mail import Message


leaveapp.config['MAIL_SERVER'] = 'smtp.gmail.com'
leaveapp.config['MAIL_PORT'] = 465

leaveapp.config['MAIL_USE_SSL'] = True,

leaveapp.config['MAIL_USERNAME'] = 'kedarasettiramarao01@gmail.com'
leaveapp.config['MAIL_PASSWORD'] = '9553491072'
leaveapp.config['ADMINS'] = ['kedarasttiramarao01@gmail.com']

mail = Mail(leaveapp)

@leaveapp.route("/")
def test():

   msg = Message('Hello', sender = 'kedarasettiramarao@gmail.com', recipients = ['kedarasttiramarao01@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

 
@leaveapp.route('/signUp')
def signUp():
    return render_template('signUp.html')


@leaveapp.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    print user
    password = request.form['password'];

    return jsonify(status='OK',user=user,password=password)


 


@leaveapp.route("/hai",methods=['GET','POST'])
def hai():
    return render_template('hai.html')


@leaveapp.route("/mgrleaverequests",methods=['GET','POST'])
def mgrleaverequests():
    reqdata = [request.form['usr'],request.form['mgr'],request.form['fromdate'],request.form['todate'],request.form['reason']]
    return render_template('mgrleaverequests.html',reqdata=reqdata)




    

session={'username':None}

@leaveapp.route("/home",methods=['GET','POST'])

def home():
    return render_template('home.html',title='Home')


@leaveapp.route("/tree",methods=['GET','POST'])

def tree():
    return render_template('thumnail.html')

@leaveapp.route("/slide",methods=['GET','POST'])

def slide():
    return render_template('slide.html')



@leaveapp.route("/empreg",methods=['GET','POST'])

def fempreg():
    user = User.query.all()
    print user
    orm = empreg()
    if request.method == 'GET':
        return render_template('empreg.html',form=orm,user=user)
    if request.method == 'POST':
        me =User()
        me.firstname = orm.empfirstname.data
        me.lastname = orm.emplastname.data
        db.session.add(me)
        db.session.commit()
        
        if  orm.empfirstname:
            return redirect('/leaveform')
    return render_template('empreg.html',form=orm,user=user)



@leaveapp.route("/M")
def m():
    user = User.query.filter_by(
            firstname='Ramarao').all()
    print user

    s= jsonify({'hai':'world'})
    print s
    return jsonify({'hai':'world'})


@leaveapp.route("/login",methods=['GET','POST'])
def login():
    form1 = LoginForm()
    print form1
    print form1.firstname
    if form1.validate():
        session['logged_in']=True
        session['username'] = form1.validate()
        print session['username']
        return redirect('/home')
    return render_template('login.html',form1=form1)
    
    
@leaveapp.route('/main')
def main():
    return render_template('main.html')


@leaveapp.route("/regleave",methods=['GET','POST'])
def regleave():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('regleave.html',form=form)
    if request.method == 'POST':
        if  form.firstname:
            return redirect('/login')
        return render_template('regleave.html',title='Registration',form=form)







@leaveapp.route("/profile",methods=['GET','POST'])
def profile():
    print session
    if session['username']:
        return render_template('profile.html',title='Profile',user=session['username'])
    else:
        return render_template('profile.html',title='Profile',user=None)




@leaveapp.route("/leaverequest",methods=['GET','POST'])
def leaverequest():
    form1 = leaveform()
    if request.method == 'GET':
        return render_template('leaverequest.html',form=form1)
    if request.method == 'POST':
        print form1.validate_on_submit()
        if  form1.validate_on_submit():
            leave = leaveform.usr,leaveform.mgr,leaveform.todate,leaveform.startdate,leaveform.reason
            print leave
            me =Post()
            me.username = leave[0]
            me.manager = leave[1]
            me.todate = leave[2]
            me.fromdate = leave[3]
            me.Reason = leave[4]
            db.session.add(me)
            db.session.commit()
        


            return redirect('/leaverequest')
        return render_template(url_for(home))


@leaveapp.route("/leavestatus")
def leavestatus():
        
        if session['username']:
            posts = Post.query.filter_by(user_id=session['username'].id).all()
            
        else:posts=None
        return render_template("leavestatus.html",title='leavestatus',posts=posts,leaveclass="danger")

@leaveapp.route("/changepassword")
def ChangePassword():
        return render_template("changepassword.html",title='Change password')


@leaveapp.route("/logout",methods=['GET','POST'])
def Logout():
    session.clear()
    return render_template("main.html",title='main')


@leaveapp.route("/lo")
def lo():
    return render_template("lo.html")
