from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from project import app
from project.forms import LoginForm, SignupForm, AdminForm
from werkzeug.urls import url_parse
from project import db
from project.forms import RegistrationForm
from project.models import User, Admin
              

@app.route('/hello') 
def hello():
    return 'Hello everyone'

@app.route('/')
@app.route('/index')
# @login_required
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
    form= SignupForm()
    if form.validate_on_submit():
       return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       return redirect(url_for('dash'))
    return render_template('login.html', title='Sign In', form=form)


    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user is None or not user.check_password(form.password.data):
    #         flash('Invalid username or password')
    #         return redirect(url_for('login'))
    #     else:
    #         flash('Successfully signed in')
    #     return redirect(url_for('dash'))
    # return render_template('login.html', title='Sign In', form=form)

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
    return render_template('adminlogin.html', title=' AdminSign In', form=form)
    







   






