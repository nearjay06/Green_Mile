from flask import render_template, flash, redirect, url_for, request, Flask, session
from .forms import LoginForm
from .models import User
from flask_login import current_user, login_user, logout_user, login_required 
from . import app, db


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
    
    return render_template('index.html', title='Home',posts=posts)

@app.route('/login', methods=['GET','POST']) 
def login():
    if current_user.is_authenticated:
        print(current_user.role)
        return redirect(url_for('index')) 
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() 
        if user is None or user.password_hash != form.password.data:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        elif (user.role == 'loader'):
            login_user(user, remember=form.remember_me.data)
            return redirect('admin')
        elif (user.role == 'supplier'):
            login_user(user, remember=form.remember_me.data)
            return redirect('admin')
        elif (user.role == 'recepient'):
            login_user(user, remember=form.remember_me.data)
            return redirect('admin')
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect('admin')       
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))






    



