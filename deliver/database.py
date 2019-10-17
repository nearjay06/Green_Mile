import psycopg2
from psycopg2.extras import RealDictCursor
from pprint import pprint
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  


class DatabaseConnection():
    
    def __init__(self):
                
        try:
            self.connection = psycopg2.connect(
                "dbname='greenmile' user='postgres' host='localhost'  port= '5432' password='123'"
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        except:
             pprint('cannot connect to database') 
       
    
    def create_table_users(self):
      create_table_command = "CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, firstname VARCHAR(20),\
                             lastname VARCHAR(20),username VARCHAR(20),email VARCHAR(50),\
                             role VARCHAR(20), password VARCHAR(10))"
      self.cursor.execute(create_table_command)
    
    # def insert_users(self, firstname ,lastname , othernames,email ,phonenumber,
                    #  username,password ,registered,isAdmin):

        # user = f"INSERT INTO user_data (firstname, lastname, othernames,email,\
                # phonenumber,username,password,registered,isAdmin) VALUES('{firstname}', '{lastname}',\
                # '{othernames}','{email}','{phonenumber}','{username}', '{password}','{registered}','{isAdmin}')\
                #  RETURNING *;"
        # pprint(user)
        # self.cursor.execute(user)
        # return self.cursor.fetchone()
                                       
    
# if __name__ == '__main__':
#    database_connection = DatabaseConnection()
#    database_connection.create_table_users()

