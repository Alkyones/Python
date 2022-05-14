# from turtle import clear
# import pandas as pd
# import numpy as np



# drh = dp.head()

# with open('DataAnalystPractice\split5\\bank-data.txt', 'a') as f:
#     #print(dp, file=f)
#     f.write(str(drh))

# print(dp.shape)

# print(dp.size)
# dp = dp.dropna()
# print(dp.size)

# dp = dp.drop(['Unnamed: 0'], axis=1)
#print(dp)

import sqlite3
import os, sys

import numpy as np
import pandas as pd


data  = pd.read_csv('DataAnalystPractice\split5\\bank-data.csv')
df_data = pd.DataFrame(data)

conn = sqlite3.connect('DataAnalystPractice\split5\\bank-data.db')
c = conn.cursor()


# c.execute("""CREATE TABLE IF NOT EXISTS bank_data (
#     id text,
#     age integer,
#     sex text,
#     region text,
#     income integer,
#     married text,
#     children integer,
#     car text,
#     save_act text,
#     current_act text,
#     mortgage text,
#     pep text)""")



# #Insert data into table which has been created 
# for row in df_data.itertuples():
#     c.execute("""INSERT INTO bank_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", 
#     [row.id,row.age, row.sex,row.region,row.income,row.married,row.children,row.car,row.save_act,row.current_act,row.mortgage,row.pep])
#     # print(row)
#     # break


# print(df_data.head())
# conn.commit()

# a = c.execute("""SELECT * FROM bank_data""").fetchall()
# print(a)
