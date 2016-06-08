import os
import re
from flask import flash,session,request,render_template,redirect,url_for,g
from leaveapp import leaveapp,db,lm,oid
from .forms import RegistrationForm,LoginForm,empreg
from functools import wraps
from .models import User,Post
leaveapp.secret_key = os.urandom(24)
import sqlite3
from sqlalchemy import and_,insert
from datetime import datetime




session={'username':None}

@leaveapp.route("/home",methods=['GET','POST'])

def home():
    return render_template('home.html',title='Home')




@leaveapp.route("/empreg",methods=['GET','POST'])

def fempreg():
    orm = empreg()
    if request.method == 'GET':
        return render_template('empreg.html',form=orm)
    if request.method == 'POST':
        print orm.empfirstname
        me =User()
        me.firstname = orm.empfirstname.data
        me.lastname = orm.emplastname.data
        for i in me:
            print me
        db.session.add(me)
        db.session.commit()
        
        if  orm.empfirstname:
            return redirect('/leaveform')
    return render_template('empreg.html',form=orm)




@leaveapp.route("/login",methods=['GET','POST'])
def login():
    form1 = LoginForm()
    print form1
    print form1.firstname
    if form1.validate():
        session['logged_in']=True
        session['username'] = form1.validate()
        
        return redirect('/profile')
    return render_template('login.html',form1=form1)
    
    
@leaveapp.route('/')
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




@leaveapp.route("/leaveform",methods=['GET','POST'])
def leaveform():
       

        return render_template('leaveform.html')


@leaveapp.route("/leavestatus")
def leavestatus():
        posts = Post.query.filter_by(
            user_id=session['username'].id).all()
        return render_template("leavestatus.html",title='leavestatus',posts=posts)

@leaveapp.route("/changepassword")
def ChangePassword():
        return render_template("changepassword.html",title='Change password')


@leaveapp.route("/logout",methods=['GET','POST'])
def Logout():
    session.clear()
    return render_template("main.html",title='main')




