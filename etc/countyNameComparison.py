import os, sys


countryDbList = []
with open("countrylist.txt") as file:
  for countryName in file:
      countryName = countryName.replace("\n", '')
      countryDbList.append(countryName)

foundFlags = os.listdir('C:\\Users\\lifeo\\Desktop\\Python\\frupro\\flags')


difference= set(countryDbList) ^ set(foundFlags)
print(difference)
print(len(difference))