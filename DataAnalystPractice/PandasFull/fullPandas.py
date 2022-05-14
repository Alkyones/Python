import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
data = pd.read_csv('DataAnalystPractice/PandasFull/full.csv')

# 1. Introduction to dataset
#print(data.head())
#print(data.shape)
#print(data.dtypes)
# checking for missing values
#print(data.isna().sum())

# 2. Which talks provoke the most online discussion?
#print(data.sort_values(by='comments',ascending=False)) #Sorts the column by the highest comment
#print(data.sort_values(by='views',ascending=True)) #returns the row with the highest views
# data['views_per_comment'] = data.views / data.comments
# print(data.sort_values('views_per_comment',ascending=False))

# 3. Which talks have the most views?
#print(data.sort_values(by='views',ascending=False))

# 3.1 newest talks first
# data['readable_date'] = pd.to_datetime(data.published_date,unit="s")
# # print(data.readable_date.sort_values(ascending=False))
# #print(data.sort_values(by='readable_date',ascending=False))

# # 3.2 plot the graph of readable date
# # date_value = data.readable_date
# # views = data.views
# # plt.plot(date_value,views)
# # plt.show() 

# data.loc[data.comments > 0,['comments','views']].plot(kind='line')
# plt.show()
# 4. Visualize the distribution of views and comments

# data.loc[data.comments < 1000 , ['comments']].plot(kind='hist',bins=20)
# #b = data.views.plot()
# plt.show()

# 5. categorize the talks by their year
# data['film_datetime'] = pd.to_datetime(data.film_date,unit='s')
# # print(data[['event','film_datetime']].sample(5))   #prints the date in the format of datetime
# # print(data['film_datetime'].dt.year.value_counts())
# # data.film_datetime.dt.year.value_counts() #Hatali cunku x axisi sortlu degil
# data.film_datetime.dt.year.value_counts().sort_index().plot #sortlu
# plt.show()