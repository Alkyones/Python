#import required modules
import sqlite3
from pathlib import Path

from numpy import true_divide


BASE_DIR = Path(__file__).parents[1]


#create a class for the database
# class Database:
#     #initialize the database
#     def __init__(self, db):
#         self.conn = sqlite3.connect(BASE_DIR / db)
#         self.c = self.conn.cursor()
#     #insert the data into the database
#     def insert(self, username, password):
#         self.c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
#         self.c.execute("INSERT INTO users VALUES(?,?)", (username, password))
#         self.conn.commit()
    
#     def show(self):
#         self.c.execute("SELECT * FROM users")
#         print( self.c.fetchall())
    
#     #login function
#     def login(self, username, password):
#         self.c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
#         if self.c.fetchall():
#             print('Login Successful')
#         else:
#             print('Login Failed')

# #insert some data to test
# new_user = Database("users.db")
# # new_user.insert("admin", "admin")
# # new_user.insert("user", "user")

# new_user.show()

# new_user.login("admin", "admin1")   


conn = sqlite3.connect(BASE_DIR / "users.db")   #connect to the database
c = conn.cursor()                              #create a cursor


# data_admin = c.execute("SELECT * FROM users WHERE username='admin' AND password='admin'")
# show_one_admin = c.fetchone()   

# data_user = c.execute("SELECT * FROM users WHERE username='user' AND password='user'")
# show_n_user = c.fetchmany(1)    

# data_all = c.execute("SELECT * FROM users")
# show_all = c.fetchall()

# print(data_admin)
# print(show_n_user)
# print(show_all)


#control flow
username = input("Enter your username: ")
password = input("Enter your password: ")

user_verify = c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)) # check if the user is in the database


if user_verify:
    print("Login Successful")
else:
    print("Login Failed")
    


