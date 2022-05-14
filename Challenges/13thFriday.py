import datetime as dt

year = input('Enter year: ')
month = input('Enter month: ')

if dt.datetime(int(year), int(month), 13).weekday() == 4:
    print('13th Friday of ' + month + ' ' + year + ' is a Friday')
else:
    print('13th Friday of ' + month + ' ' + year + ' is not a Friday')