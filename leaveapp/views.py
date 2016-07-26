import os
import re
from flask import flash,session,request,render_template,redirect,url_for,g,jsonify, send_from_directory
from leaveapp import leaveapp,db
from .forms import RegistrationForm,LoginForm,empreg,leaveform,search
from functools import wraps
from .models import User,Post,Calendar,Birthday
leaveapp.secret_key = os.urandom(24)
import sqlite3
from sqlalchemy import and_,insert
from datetime import datetime
from werkzeug import secure_filename

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
print "APP_ROOT",APP_ROOT
# Route that will process the file upload
@leaveapp.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, r'images')
    print target
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print request.files.getlist('file')
    print dir(request.files.getlist)
    for upload in request.files.getlist('file'):
        print upload
        print("{} is the file name".format(upload.filename))
        filename=upload.filename
        destination="\\".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
    return render_template("profile.html",imagename=filename,title='Profile',user=session['username'])

@leaveapp.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory('images',filename)
    

# This is the path to the upload directory
leaveapp.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
leaveapp.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in leaveapp.config['ALLOWED_EXTENSIONS']


@leaveapp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(leaveapp.config['UPLOAD_FOLDER'],
                               filename)




@leaveapp.route('/index')
def index():
    return render_template('index.html')

@leaveapp.route('/filter')
def filter():
    user = User.query.filter_by(
            firstname='Ramarao').all()
    return render_template('filter.html',users=user)


 
@leaveapp.route('/echo/', methods=['GET'])
def echo():
    print request.args.get('echoValue')
    user = User.query.filter_by(
            firstname=request.args.get('echoValue')).all()
    print user
    ret_data = {"value":[user[0].lastname,user[0].firstname],"value1":'Ramarao'}
    return jsonify(ret_data)





@leaveapp.route('/empprofile')
def signup():
    return render_template('empprofile.html')





 




@leaveapp.route("/mgrleaverequests",methods=['GET','POST'])
def mgrleaverequests():
    reqdata = [request.form['usr'],request.form['mgr'],request.form['fromdate'],request.form['todate'],request.form['reason']]
    return render_template('mgrleaverequests.html',reqdata=reqdata)




    

session={'username':None}

@leaveapp.route("/home",methods=['GET','POST'])

def home():
    print datetime.now()
    leave=Post.query.filter_by(user_id=session['username'].id).first()
    print leave
    print leave.Availableleaves

    birthdays = Birthday.query.all()



    days = Calendar.query.all()
    return render_template('home.html',title='Home',days=days,Birthdays = birthdays,leave=leave)


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
            firstname='Saidatta').first()
    print user
    return jsonify({'name':user.firstname})

@leaveapp.route("/",methods=['GET','POST'])
@leaveapp.route("/login",methods=['GET','POST'])
def login():
    form1 = LoginForm()
    print form1
    
    if request.method == 'POST':
    
        if form1.validate() == False:
            print form1.firstname.data
            print form1.password.data
            print form1.user
            
            
            print session['username']
            return render_template('login.html',form1=form1)
        else:  
            session['logged_in']=True
            session['username'] = form1.validate()
            return redirect('/home')
    else:   
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
        return render_template('leaverequest.html',form=form1,user=session['username'])
    if request.method == 'POST':
        print "form1.validaterequest()",form1.validaterequest()
        if  form1.validaterequest():
            leavefileds = form1.validaterequest()
            me =Post()
            me.username = leavefileds[0]
            me.manager = leavefileds[1]
            me.todate = leavefileds[2]
            me.fromdate = leavefileds[3]
            me.Reason = leavefileds[4]
            
            db.session.add(me)
            db.session.commit()
            

            return render_template('leaverequest.html',form=form1,user=session['username'])
        return redirect('/home')


@leaveapp.route("/leavestatus",methods=['GET','POST'])
def leavestatus():
    form = search()
    if request.method == 'GET': 
        if session['username']:
            posts = Post.query.filter_by(user_id=session['username'].id).all()
            print posts         
        else:
            posts=None
            print posts
    else:
    
        try:
            posts = Post.query.filter_by(user_id=session['username'].id).order_by(form.search.data).all()
        except:
            posts = posts
                
            
        print posts
       

        
    return render_template("leavestatus.html",title='leavestatus',posts=posts,leaveclass="danger",form=form)

@leaveapp.route("/changepassword")
def ChangePassword():
        return render_template("changepassword.html",title='Change password')


@leaveapp.route("/logout",methods=['GET','POST'])
def Logout():
    session.clear()
    return render_template("main.html",title='main')



