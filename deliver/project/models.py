from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import db,login

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True,unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    role = db.Column(db.String(20), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True
    
    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

class Supplier(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True,unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    role = db.Column(db.String(20), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    def __repr__(self):
        return '<Supplier {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True
    
    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

class Loader(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True,unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    role = db.Column(db.String(20), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    def __repr__(self):
        return '<Loader {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True
    
    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False


class Recepient(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True,unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    role = db.Column(db.String(20), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    def __repr__(self):
        return '<Recepient {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True
    
    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

class Admin(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True,unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    role = db.Column(db.String(20), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Admin {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


