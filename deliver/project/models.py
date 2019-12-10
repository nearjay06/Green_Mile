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
    packages=db.relationship('Package',backref='package_creator',lazy = True)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    
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


class Package(db.Model):
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    date=db.Column(db.DateTime, index=True,unique=True,default=datetime.today)
    item=db.Column(db.String(100), index=True,unique=True)
    quantity=db.Column(db.String, index=True,unique=True)
    recepient=db.Column(db.String(20), index=True,unique=True)
    recepient_email=db.Column(db.String(100), index=True,unique=True)
    recepient_phone=db.Column(db.String(20), index=True,unique=True)
    duration_of_delivery=db.Column(db.String(20), index=True,unique=True)
    pickup_location=db.Column(db.String(20), index=True,unique=True) 
    droppoff_location=db.Column(db.String(20), index=True,unique=True)
    destination=db.Column(db.String(20), index=True,unique=True)
    transport_mode=db.Column(db.String(20), index=True,unique=True)      
    cost=db.Column(db.String(100), index=True,unique=True)
    delivery_status=db.Column(db.String(20), index=True,unique=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)      


    def __repr__(self):
        return '<Package {}>'.format(self.id)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))





