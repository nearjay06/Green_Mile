from flask import render_template,flash, redirect, url_for, request, Flask, session
from flask_login import current_user, login_user, logout_user, login_required
from project import app, db
from project.forms import LoginForm,SignupForm, AdminForm
from werkzeug.urls import url_parse
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import re
import psycopg2
from psycopg2.extras import RealDictCursor
from  usermodels import UserModels
from database import DatabaseConnection
database_connection = DatabaseConnection() 

@app.route('/hello') 
def hello():
    return 'Hello everyone'

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Client'}
    posts = [
        {
            'author': {'username': 'Client'},
            'body':'Welcome to Green Mile'

        }

    ]
    return render_template('index.html', title='Home Page', user=user,posts=posts)
  
@app.route('/signup', methods=['GET','POST']) 
def signup():
    form = SignupForm()
    msg = ''
        
    if request.method == 'POST' and 'firstname' in request.form and 'lastname' in request.form and 'username' in request.form and 'email' in request.form and 'role' in request.form and 'password' in request.form  and 'confirmpassword' in request.form:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        email = request.form['email']
        role = request.form['role']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword'] 
        
        register_user = UserModels.insert_users(firstname,lastname,username,email,role,password)
        if register_user:
            db.session.add(register_user)
            db.session.commit()
            return redirect(url_for('admin'))
        else:
            msg = 'Please sign up first!'
            return redirect(url_for('signup'))      
    return render_template('signup.html',title='Sign Up', form=form, msg=msg, users = users) 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        login_users = UserModels.login_users(username, password) 
        if login_users:
            session['loggedin'] = True
            # session['id'] = users['id']
            # session['username'] = users['username']
            # session['password'] = users['password'] 
            # return 'Signed in successfully!'
        else:
          msg = 'Incorrect username or password!'
        return redirect(url_for('dash'))
    return render_template('login.html', title='Sign In', form=form, msg=msg)


@app.route('/dash', methods=['GET', 'POST'])
def dash():
    return render_template('dash.html', title='Dash') 

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# @app.route('/logout')
# def logout():
#     session.pop('loggedin', None)
#     session.pop('id', None)
#     session.pop('username', None)
#    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admindash.html', title='AdminPage') 

@app.route('/adminlogin', methods=['GET','POST'])
def adminlogin():
    form = AdminForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(Adminusername=form.Adminusername.data).first()
        if admin is None or not admin.check_password(form.password.data):
            flash('Invalid username or password')
        return redirect(url_for('adminlogin'))
    return render_template('adminlogin.html', title='AdminSign In', form=form)
    

@app.route('/users', methods=['GET', 'POST'])
def users():
    try:
        connection = psycopg2.connect(
                "dbname='greenmile' user='postgres' host='localhost'  port= '5432' password='123'"
            )
        cursor = connection.cursor(cursor_factory=RealDictCursor)    
        query = "SELECT * from users"
        cursor.execute(query)
        userDetails = cursor.fetchall()
        cursor.close()
        return render_template('users.html', userDetails=userDetails,title='Users') 
    except Exception as e:
        return (str(e))

@app.route('/suppliers', methods=['GET', 'POST'])
def suppliers():
    try:
        connection = psycopg2.connect(
                "dbname='greenmile' user='postgres' host='localhost'  port= '5432' password='123'"
            )
        cursor = connection.cursor(cursor_factory=RealDictCursor)    
        query = "SELECT * from suppliers"
        cursor.execute(query)
        suppliers = cur.fetchall()
        cursor.close()
        return render_template('suppliers.html', suppliers=suppliers,title='Suppliers')
    except Exception as e:
        return (str(e))
    

@app.route('/loaders', methods=['GET', 'POST'])
def loaders():
    try:
        connection = psycopg2.connect(
                "dbname='greenmile' user='postgres' host='localhost' port= '5432' password='123'"
            )
        cursor = connection.cursor(cursor_factory=RealDictCursor)    
        query = "SELECT * from loaders"
        cursor.execute(query)
        loaders = cursor.fetchall()
        cursor.close()
        return render_template('loaders.html', loaders=loaders,title='Loaders') 
    except Exception as e:
        return (str(e))






