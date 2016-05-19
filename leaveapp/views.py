import os
import re
from flask import flash,session,request,render_template,redirect,url_for,g
from leaveapp import leaveapp,db,lm,oid
from .forms import RegistrationForm,LoginForm
from functools import wraps
from .models import User
leaveapp.secret_key = os.urandom(24)
import sqlite3






@leaveapp.route("/home",methods=['GET','POST'])

def home():
    return render_template('home.html',title='Home')

@leaveapp.route("/login",methods=['GET','POST'])
def login():
    form1 = LoginForm()
    error = None
    if request.method == 'GET':
        return render_template('login.html',form1=form1)
    else:
    
        if request.method == 'POST':
            
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
    if request.method == 'POST':
        if  form.validate_on_submit():
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
def Logout():
    form1 = LoginForm()
    session.pop('logged_in',None)
    print session
    return render_template("login.html",title='regleave',form1=form1)



