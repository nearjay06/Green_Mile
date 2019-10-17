from flask import Flask 
from database import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from database  import DatabaseConnection
from database import Config


database_connection= DatabaseConnection()
database_connection.create_table_users()

app = Flask(__name__) 
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'



from project import routes,models


