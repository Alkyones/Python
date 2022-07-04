#import required modules
import sqlite3
from pathlib import Path
import unittest

from login_sys import login

#create a class for testing

class TestCase(unittest.TestCase):
    #initialize the database
    def setUp(self):
        #create cur and conn
        pass

    def login_valid(self):
        #check if the user is in the database and function works correctly
        pass

    def login_invalid(self):
        #check if the user is not in the database and function works correctly
        pass