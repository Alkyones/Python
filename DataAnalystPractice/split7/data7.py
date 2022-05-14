import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#veriyi oku ve bir line plotu ciz her sinifta kactane ogrenci oldugunu gosteren
data = pd.read_excel("DataAnalystPractice\split7\student.xlsx")
# df = data['class'].value_counts()
# print(df)
# df.plot(kind='line')
# plt.show()

#plot bar graph showing class and its mean mark for each class
# df = data[['class','mark']].groupby('class').mean()
# print(df)
# df.plot(kind='bar',title='Mean Mark for each class')
# plt.show()

#plot bar graph showung class and its mean mark and maximum mark of each class
# df = data[['class','mark']].groupby('class').agg(['mean','max'])
# df.plot(kind='bar',title='Mean Mark and Maximum Mark for each class')
# plt.show()

#plot a pie chart showing class and number of students
# df = data['class'].value_counts()
# df.plot(kind='pie',title='Number of Students for each class')
# print(df)
# plt.show()

#create a density graph using mark
# df = data['mark']
# df.plot(kind='line',title='Density Graph of Mark')

# plt.show()

#create a data random int and price
import sqlite3
from random import randint
conn = sqlite3.connect('DataAnalystPractice\split7\data.db')
c = conn.cursor()

# c.execute("""CREATE TABLE car_price(car_year INT, car_price INT)""")
# for i in range(10):
#     c.execute(f"""INSERT INTO car_price VALUES(?,?)""",(randint(2000,2022),randint(10000,50000)))
# conn.commit()

# datayi pandaya cek
# data = pd.read_sql_query("SELECT * FROM car_price",conn)
# df = data.sort_values(by='car_year',ascending=False)


# yillara gore fiyat ortalamasi
# df = data[['car_year','car_price']].groupby('car_year').agg(['mean','max','min'])
# plt.show()
# print(df)

#Hometask

#1. Create a database with table insan adi , yasi , cinsiyeti ve isi 100 tane
#2. pandaya cek
#3. plot pie chart showing gender quantity
#4. cinsiyetlerin yas ortalamasi
#5. 5 den fazla olan islerin bar grafigi
#