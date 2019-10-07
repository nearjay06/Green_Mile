from flask import Flask 
from config import Config
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

db = SQLAlchemy(app)
app.config.from_object(Config)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'




from project import routes,models


