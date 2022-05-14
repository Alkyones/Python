import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#a = pd.Series(['hello','world','my','name','is','Anna'])


# built in
#b = a.apply(len)

#map version
# b = a.map(len)  #map is a built in function
# print(b)

#acemice
# b = zip(a ,map(len,a))
# print(list(b))

# c = map(list,zip(a,b))
# print(list(c))
#------------------------------------------------------

#a = pd.Series( [1,'Orange',2,4,'money',5,'phone'])
# kac tane string kac tane integer
# b = a[a.map(lambda x: type(x) == str)].count()
# intlist = a.count() - b
# print(intlist)

#------------------------------------------------------
#1 create a database of cars implement 10 cars into that , car name , price , year , color
#2 use pandas to count how many cars have the color red

# use pandas to get the newest car

# plot graph of price cars

# plot graph of price cars by year