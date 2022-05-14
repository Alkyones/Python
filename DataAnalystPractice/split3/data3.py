import pandas as pd
import numpy as np
import sqlite3
from faker import Faker


fake = Faker()
conn = sqlite3.connect('data.db')
c = conn.cursor()

# initialize the database
# a = c.execute("SELECT namep FROM person").fetchall()
# name_person = []
# for i in a:
#     name_person.append(i[0])

# a = c.execute("SELECT age FROM person").fetchall()
# age_person = []
# for i in a:
#     age_person.append(i[0])
# print(age_person)


# people = pd.Series(age_person, index=name_person)
# print(people)

# #multi initialize
# a = c.execute("SELECT namep,age FROM person").fetchall()
# person = []

# for prs in a:
#     person.append([prs[0],prs[1]])

# print(person)
# people_panda = pd.Series([age[1] for age in person], index=[name[0] for name in person])
# print(people_panda)

a = c.execute("SELECT namep,age FROM person").fetchall()

df = pd.DataFrame(a, columns=['namep', 'age'])
df.index = [f'person{i}' for i in range(1,len(df)+1)]
df.to_excel('data.xlsx')

# import mysql.connector
# db = mysql.connector.connect(
#     host="serverIP",
#     user="kullaniciAdi",
#     passwd="sifre",
#     database="veritabaniAdi")
    