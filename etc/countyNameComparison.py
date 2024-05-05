import os, sys


countryDbList = []
with open("countrylist.txt") as file:
  for countryName in file:
      countryName = countryName.replace("\n", '')
      countryDbList.append(countryName)

foundFlags = os.listdir('your_flags_path')


difference= set(countryDbList) ^ set(foundFlags)
print(difference)
print(len(difference))