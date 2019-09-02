from flask import render_template, flash, redirect, url_for
from project import app
from project.forms import LoginForm, SignupForm

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
    return render_template('index.html', title='Home', user=user,posts=posts)
  
@app.route('/signup')
def signup():
    form= SignupForm()
    if form.validate_on_submit():
        flash('Signup requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/dash', methods=['GET', 'POST'])
def dash():
    return render_template('dash.html', title='Dash') 