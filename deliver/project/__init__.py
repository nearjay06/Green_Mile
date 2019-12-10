from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from ..config import Config
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt 


app = Flask(__name__) 
app.config.from_object(Config)
db = SQLAlchemy(app)
app.config['FLASK_ADMIN_SWATCH'] = 'flatly' 
admin = Admin(app, name='Greenmile ', template_mode='bootstrap3')
bcrypt = Bcrypt(app) 

migrate = Migrate(app, db)
 
login_manager = LoginManager(app)
login_manager.login_view='login'

from . import routes, models
# from deliver.project.models import Users, Suppliers, Loaders, Recepients 
from deliver.project.models import User, Package


class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        user_list_url = url_for('logout')
        return redirect(user_list_url)

# class LoaderModelView(ModelView):
#     can_delete = False 
#     can_create = False 
#     can_update = False

#     def is_accessible(self):
#         return current_user.is_authenticated and (current_user.role == 'loader' or current_user.role == 'admin')

# class SupplierModelView(ModelView):
#     def is_accessible(self):
#         return current_user.is_authenticated and (current_user.role == 'supplier' or current_user.role == 'admin')

# class RecepientModelView(ModelView):
#     can_delete = False 
#     can_create = False 
#     can_update = False

#     def is_accessible(self):
#         return current_user.is_authenticated and (current_user.role == 'recepient' or current_user.role == 'admin')
        
class UserView(ModelView):
    column_exclude_list = ['password_hash']
    form_choices={
        'role':[
            ('Admin','Admin'),
            ('Supplier', 'Supplier'),
            ('Loader','Loader'),
            ('Recepient','Recepient') 
        ]
    }
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == 'Admin'  

class PackageView(ModelView):
    column_exclude_list = ['password_hash']

    def is_accessible(self):
        return current_user.is_authenticated
     
           

     

admin.add_view(UserView(User, db.session))
admin.add_view(PackageView(Package, db.session))
admin.add_view(AnalyticsView(name='Logout', endpoint='logout')) 






