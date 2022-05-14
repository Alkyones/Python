import faker
import numpy as np
import sys
from faker import Faker
import sqlite3


# a = []
# for i in range(10):
#     a.append(i)

# b = np.array(a)

# print(len(a))
# print(len(b))

# print(sys.getsizeof(a))
# print(sys.getsizeof(b))


# net incomes
#a  = [x for x in range(1,477233)]

# income + salary
#salary = 5

#new list
# 10 \ 9
#b = [x + salary for x in a]
# 10 \ 5
# b = []
# #yeni liste brut gelir ve aylik gelir
# for income in a:
#     b.append(income + salary)

# #a = np.array(a) + salary

# print(b)

# a = [x for x in range(1,7)]

# for i in range(len(a)):
#     if i > 2:
#         print(a[i])

#database 
conn = sqlite3.connect('DataAnalystPractice\split2\data.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS person(namep text, age integer)""")

fake = Faker()

for i in range(10):
    c.execute("INSERT INTO person(namep,age) VALUES(?,?)",[fake.name(), fake.random_int(min=1,max=90)])

a = c.execute("SELECT * FROM person").fetchall()

for row in a:
    print(row)