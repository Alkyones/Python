# import pandas as pd
# import numpy as np


# 1- How to create panda series from python listo or numpy array

# ex_list = list('abcdefghijklmnopqrstuvwxyz')
# pseri   = pd.Series(ex_list)
# pseri.index = [i for i in range(1,len(ex_list)+1)]
#print(pseri)

# 2- How to combine more than one series into one

# ex = pd.Series([1,2,3,4,5,6,7,8,9,10])
# ex2 = pd.Series([11,12,18,19,20])
# ex3 = pd.Series([21,24,25,26,27,28,29,30])
# #solution 1
# #ex_total = pd.concat([ex,ex2,ex3],axis=1) 
# # solution 2
# ex_total = pd.DataFrame({'column0': ex, 'column1': ex2, 'column2': ex3})
# print(ex_total)

# 3- How to assingn name to panda series

# ex = pd.Series([1,2,3,4,5,6,7,8,9,10],name='numbers')
# ex.name = 'numbersNew'
# print(ex)

# 4- How to get median , max , min and 25th of percentile of a series

# ex = pd.Series(np.arange(1,100))
# print(ex.min(),ex.max(),ex.median(),ex.mean(),np.percentile(ex,q=[0,25,50,75,100]))

# # 5- How to check frequency of item in list
# ex = pd.Series(np.take(list('abcdefget'),np.random.randint(8,size=50)))

# print(ex.value_counts())

# 6- how to check the frequency and if its lower than N then change it to another value 
# nAn = 'other'
# ex = pd.Series(np.random.randint(1,5,size=12))
# ex[~ex.isin(ex.value_counts().index[:2])] = nAn
# print(ex)

# 7- how to conver data series to data frame in pandas

# ds = pd.Series([1,2,3,4,5,6,7,8,9,10])
# df = pd.DataFrame(ds.values.reshape(5,2))
# print(df)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 8 - np.Argwhere * find all items can be divided by 3
# ds = pd.Series(np.random.randint(1,10,7))
# print(
# np.argwhere(ds % 2 == 0))

# 9 - how to implement elements vertically and horizantally
# ser1 = pd.Series(range(5))
# ser2 = pd.Series(list('abcde'))

# #vertical 
# # ser3 = ser1.append(ser2)
# # print(ser3)

# #horizontal
# ser3 = pd.concat([ser1,ser2],axis = 1)
# print(ser3)