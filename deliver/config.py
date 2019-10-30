
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret'
    # SQLALCHEMY_DATABASE_URI='postgresql://postgres:123@localhost:5432/greenmile' or 'postgres://ksusrzldvxxlns:7424f9ba3105d6a2246bdb20faeb1fb247b11ff0cff6eb5004b4cf73e2b4fc9c@ec2-50-19-95-77.compute-1.amazonaws.com:5432/d9lvi2d7ml0i9d'
    SQLALCHEMY_DATABASE_URI= 'postgres://ksusrzldvxxlns:7424f9ba3105d6a2246bdb20faeb1fb247b11ff0cff6eb5004b4cf73e2b4fc9c@ec2-50-19-95-77.compute-1.amazonaws.com:5432/d9lvi2d7ml0i9d'
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



