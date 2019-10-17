import datetime
from pprint import pprint 
from psycopg2.extras import RealDictCursor
from database import DatabaseConnection
connection = DatabaseConnection()

class UserModels():
    @staticmethod
    def insert_users(firstname,lastname,username,email,role,password):

        user = f"INSERT INTO users (firstname, lastname, username,email,\
                role,password) VALUES('{firstname}', '{lastname}',\
                '{username}','{email}','{role}','{password}')\
                RETURNING *;"
        pprint(user)
        connection.cursor.execute(user)
        return connection.cursor.fetchone()

    @staticmethod
    def login_users(username, password):

        user = f"INSERT INTO users (username, password) VALUES('{username}', '{password}')\
                RETURNING *;"
        pprint(user)
        connection.cursor.execute(user)
        return connection.cursor.fetchone()

    @staticmethod
    def get_users(self):
    
        query = """SELECT * FROM users""" 
        self.cursor.execute(query)
        return self.cursor.fetchall()  

    @staticmethod
    def get_specific_user(self,username,password):
        
        query = """SELECT username FROM users WHERE username = '{}' AND password = '{}'""".format(username, password) 
        self.cursor.execute(query)
        return self.cursor.fetchone() 



                                       
# class UserModels():
#     @staticmethod
#     def insert_users():
#         date_created= datetime.datetime.utcnow() 

#         user = f"INSERT INTO users (firstname, lastname, username,email,\
#                 role,password,registered) VALUES('joan', 'okecho',\
#                 'jojo','jay@example.com','admin','password','date_created')\ 
#                     RETURNING *;"
#         pprint(user)
#         connection.cursor.execute(user)
#         return connection.cursor.fetchone()


                                