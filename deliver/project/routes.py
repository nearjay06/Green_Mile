from flask import render_template,flash, redirect, url_for, request, Flask, session
from flask_login import current_user, login_user, logout_user, login_required
from project import app
from project.forms import LoginForm,SignupForm, AdminForm
from werkzeug.urls import url_parse
from project import db
from project.models import User, Admin
from config import Config

# from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app.secret_key = 'my secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'newuser'
app.config['MYSQL_PASSWORD'] = 'apples'
app.config['MYSQL_DB'] = 'greenmile'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# app.config['SQLAlchemy_DATABASE_URI'] = "mysql://newuser:apples@localhost/greenmile"


mysql = MySQL(app)

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
  
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate():
        user = User(form.firstname.data,form.lastname.data,form.username.data, form.email.data,
                    form.password.data,form.confirmpassword.data)
        db_session.add(user)
        flash('Thanks for signing up')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

    # user = User.query.filter_by(username=form.username.data).first()
    # msg = ''
    # if request.method == 'POST' and 'firstname' in request.form and 'lastname' in request.form and 'username' in request.form and 'email' in request.form and 'password' in request.form  and 'confirmpassword' in request.form:
        
    #     firstname = request.form['firstname']
    #     lastname = request.form['lastname']
    #     username = request.form['username']
    #     email = request.form['email']
    #     password = request.form['password']
    #     confirmpassword = request.form['password']
    #     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    #     cursor.execute('SELECT * FROM users WHERE username = %s AND firstname = %s AND lastname = %s AND email = %s AND password= %s AND confirmpassword = %s', (username, firstname,lastname,password,confirmpassword))
    #     users = cursor.fetchone()
    # elif request.method == 'GET':
    #     msg = 'Please first signup!'
    #     if users:
    #         msg = 'Account already exists!'
    #     elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
    #         msg = 'Invalid email address!'
    #     elif not re.match(r'[A-Za-z0-9]+', username):
    #         msg = 'Username must contain only characters and numbers!'
    #     elif not username or not password or not email:
    #         msg = 'Some details may be missing'
    #     else:
    #         cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s, %s, %s, %s)', (firstname,lastname,username, email,password, confirmpassword))
    #         mysql.connection.commit()
    #         msg = 'Successfully signedup'
    
    # return render_template('signup.html',title='Sign Up', msg=msg)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password1 = %s', (username, password))
        users = cursor.fetchone()
        if users:
            session['loggedin'] = True
            session['id'] = users['id']
            session['username'] = users['username']
            return 'Signed in successfully!'
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
        cur = mysql.connection.cursor()
        query = "SELECT * from users"
        cur.execute(query)
        userDetails = cur.fetchall()
        cur.close()
        return render_template('users.html', userDetails=userDetails,title='Users') 
    except Exception as e:
        return (str(e))


@app.route('/suppliers', methods=['GET', 'POST'])
def suppliers():
    try:
        cur = mysql.connection.cursor()
        query = "SELECT * from suppliers"
        cur.execute(query)
        suppliers = cur.fetchall()
        cur.close()
        return render_template('suppliers.html', suppliers=suppliers,title='Suppliers') 
    except Exception as e:
        return (str(e))
    

@app.route('/loaders', methods=['GET', 'POST'])
def loaders():
    try:
        cur = mysql.connection.cursor()
        query = "SELECT * from loaders"
        cur.execute(query)
        loaders = cur.fetchall()
        cur.close()
        return render_template('loaders.html', loaders=loaders,title='Loaders') 
    except Exception as e:
        return (str(e))






