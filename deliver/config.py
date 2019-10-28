
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI') or 'postgresql://postgres:123@localhost:5432/greenmile'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True



