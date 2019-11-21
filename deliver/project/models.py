# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import db,login_manager
from sqlalchemy import Integer, Sequence
from flask_admin import BaseView, expose
from deliver.project import bcrypt
from sqlalchemy import event
from flask_bcrypt import generate_password_hash


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), index=True,unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    role = db.Column(db.String(20), index=True, unique=False)
    password_hash = db.Column(db.String(128))
    isAdmin = db.Column(db.Boolean, default = False) 
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # def check_password(self,password):
    #     return check_password_hash(self.password_hash, password)

    def check_password(self,password):
        return self.password_hash

    def is_active(self):
        return True
    
    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False


@event.listens_for(User.password_hash, 'set', retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        return bcrypt.generate_password_hash(value)
    return value

class Supplier(db.Model):
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    date=db.Column(db.Integer, index=True,unique=True)
    time=db.Column(db.Integer, index=True,unique=True)
    item=db.Column(db.String(20), index=True,unique=True)
    recepient=db.Column(db.String(20), index=True,unique=True)       
    pickup_location=db.Column(db.String(20), index=True,unique=True)         
    destination=db.Column(db.String(20), index=True,unique=True)         
    status=db.Column(db.String(20), index=True,unique=True)         
    invoices_paid=db.Column(db.Integer, index=True,unique=True)        
    invoices_pending=db.Column(db.Integer, index=True,unique=True)    

    def __repr__(self):
        return '<Supply {}>'.format(self.id)

    
class Loader(db.Model):
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    date=db.Column(db.Integer, index=True,unique=True)
    time=db.Column(db.Integer, index=True,unique=True)
    items_requested=db.Column(db.String(20), index=True,unique=True)         
    quantity=db.Column(db.Integer, index=True,unique=True)
    recepient=db.Column(db.String(20), index=True,unique=True)            
    pickup_location=db.Column(db.String(20), index=True,unique=True) 
    destination=db.Column(db.String(20), index=True,unique=True)
    transportation=db.Column(db.String(20), index=True,unique=True)      
    cost=db.Column(db.Integer, index=True,unique=True)


    def __repr__(self):
        return '<Load {}>'.format(self.id)

class Recepient(db.Model):
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    date=db.Column(db.Integer, index=True,unique=True)
    time=db.Column(db.Integer, index=True,unique=True)
    duration_of_delivery=db.Column(db.String(20), index=True,unique=True)
    item_delivered=db.Column(db.String(20), index=True,unique=True)
    pickup_location=db.Column(db.String(20), index=True,unique=True) 
    destination=db.Column(db.String(20), index=True,unique=True)

    def __repr__(self):
        return '<Receive {}>'.format(self.id)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


