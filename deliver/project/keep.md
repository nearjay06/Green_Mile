import psycopg2
from psycopg2.extras import RealDictCursor

<a href="{{url_for('users')}}"> Recepients </a>
<a href="{{url_for('suppliers')}}"> Suppliers</a>
<a href="{{url_for('loaders')}}"> Loaders </a>
<a href="{{url_for('recepients')}}"> View Recepients </a> <br>
<a href="{{url_for('suppliers')}}"> View Suppliers</a> <br>
 <a href="{{url_for('loaders')}}"> View Loaders </a> <br>


import psycopg2
from psycopg2.extras import RealDictCursor 
from pprint import pprint

# class DatabaseConnection():
    
#     def __init__(self):
                
#         try:
#             self.connection = psycopg2.connect(
#                 "dbname='greenmile' user='postgres' host='localhost'  port= '5432' password='123'"
#             )
#             self.connection.autocommit = True
#             self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
#         except:
#              pprint('cannot connect to database') 
       
    
    def create_table_users(self):
       create_table_command = "CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, \
                              username VARCHAR(20),email VARCHAR(50),\
                            role VARCHAR(20), password VARCHAR(10))"
      self.cursor.execute(create_table_command)
    
   
# if __name__ == '__main__':
#    database_connection = DatabaseConnection()
#    database_connection.create_table_users()

