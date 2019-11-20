from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from ..config import Config
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView 


app = Flask(__name__) 
app.config.from_object(Config)
db = SQLAlchemy(app)
app.config['FLASK_ADMIN_SWATCH'] = 'flatly'
admin = Admin(app, name='greenmile Admin', template_mode='bootstrap3')

migrate = Migrate(app, db)
 
login_manager = LoginManager(app)
login_manager.login_view='login'

from . import routes, models
from deliver.project.models import User, Supplier, Loader, Recepient

class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        user_list_url = url_for('logout')
        return redirect(user_list_url)

class LoaderModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and (current_user.role == 'loader' or current_user.role == 'admin')


class SupplierModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and (current_user.role == 'supplier' or current_user.role == 'admin')

class RecepientModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and (current_user.role == 'recepient' or current_user.role == 'admin')

class UserView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == 'admin'
    
    
   
admin.add_view(UserView(User, db.session))
admin.add_view(LoaderModelView(Loader, db.session))
admin.add_view(SupplierModelView(Supplier, db.session))
admin.add_view(RecepientModelView(Recepient, db.session))
admin.add_view(AnalyticsView(name='Logout', endpoint='logout')) 






