import sqlite3
from faker import Faker


#database connection 
conn = sqlite3.connect('SOFTWAREPython\CustomerData.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Customers(Customer_Name TEXT, Customer_Age INTEGER, Customer_City TEXT)""")

iteration_count = int(input('Enter how many fake data you want to generate: '))

for i in range(iteration_count):
    fake = Faker()
    c.execute("INSERT INTO Customers(Customer_Name, Customer_Age, Customer_City) VALUES (?,?,?)",
              (fake.name(), fake.random_int(1,100), fake.city()))

conn.commit()
conn.close()