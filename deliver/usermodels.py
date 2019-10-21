import datetime
from pprint import pprint 
from psycopg2.extras import RealDictCursor
from database import DatabaseConnection
connection = DatabaseConnection()

class UserModels():
    @staticmethod
    def insert_users(username,email,role,password):

        user = f"INSERT INTO users (username,email,\
                role,password) VALUES(\
                '{username}','{email}','{role}','{password}')\
                RETURNING *;"
        connection.cursor.execute(user)
        return "user registered successfully"

    @staticmethod
    def login_users(username, password):

        user = f"INSERT INTO users (username, password) VALUES('{username}', '{password}')\
                RETURNING *;"
        connection.cursor.execute(user)
        return connection.cursor.fetchone()

    @staticmethod
    def get_users(self):
    
        query = """SELECT * FROM users""" 
        self.cursor.execute(query)
        return self.cursor.fetchall()  

    
    @staticmethod
    def get_suppliers(self):
    
        query = """SELECT * FROM suppliers""" 
        self.cursor.execute(query)
        return self.cursor.fetchall()  
    
    
    @staticmethod
    def get_loaders(self):
        query = """SELECT * FROM loaders""" 
        self.cursor.execute(query)
        return self.cursor.fetchall()  
    
       
    @staticmethod
    def get_specific_user(self,username,password):
        
        query = """SELECT username FROM users WHERE username = '{}' AND password = '{}'""".format(username, password) 
        self.cursor.execute(query)
        return self.cursor.fetchone() 


                                