from flask import render_template, flash, redirect, url_for, request, Flask, session
from .forms import LoginForm, RegistrationForm, AdminForm
from .models import User, Supplier, Loader, Recepient 
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
        return redirect(url_for('index')) 
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        return redirect(url_for('recepdash')) 
    return render_template('login.html', title='Sign In', form=form)

@app.route('/adminlogin', methods=['GET','POST'])
def adminlogin():
    form = AdminForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(Adminusername=form.Adminusername.data).first()
        if admin is None or not admin.check_password(form.password.data):
            flash('Invalid username or password')
        return redirect(url_for('adminlogin'))
    return render_template('adminlogin.html', title='AdminSign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you have registered a user!')
        return redirect(url_for('admin'))
    return render_template('register.html', title='Register', form=form)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    user = User.query.order_by(User.username).all()
    print (user)     
    
    return render_template('admindash.html', user=user, title='AdminPage') 

@app.route('/dash', methods=['GET', 'POST'])
def dash():
    return render_template('dash.html', title='Dash') 


@app.route('/recepdash', methods=['GET', 'POST'])
def recepdash():
    return render_template('recepdash.html', title='recepdash') 

@app.route('/supdash', methods=['GET', 'POST'])
def supdash():
    return render_template('supdash.html', title='supdash') 

@app.route('/loadash', methods=['GET', 'POST'])
def loadash():
    return render_template('loadash.html', title='loadash') 

@app.route('/users', methods=['GET', 'POST'])
def users():
    user = User.query.order_by(User.username).all()
    print (user)     
    
    return render_template('users.html', userDetails=users,title='Users') 
   

@app.route('/suppliers', methods=['GET', 'POST'])
def suppliers():
    supplier = Supplier.query.order_by(Supplier.username).all()
    print (supplier)     
    

    return render_template('suppliers.html', suppliers=suppliers,title='Suppliers')
    

@app.route('/loaders', methods=['GET', 'POST'])
def loaders():
    loader = Loader.query.order_by(Loader.username).all()
    print (loader)       
    return render_template('loaders.html', loaders=loaders,title='Loaders') 
    

@app.route('/recepients', methods=['GET', 'POST'])
def recepients():
    recepient = Recepient.query.order_by(Recepient.username).all()
    print (recepient)      
    
    return render_template('recepients.html', recepients=recepients,title='Recepients') 
    



    