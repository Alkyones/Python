import sqlite3

#database connection 
conn = sqlite3.connect('SOFTWAREPython\CustomerData.db')
c = conn.cursor()

class Singleton:
    __instance = None

    def __new__(cls):
        if Singleton.__instance is None:
            cls.__instance = \
                super(Singleton, cls).__new__(cls)
        return cls.__instance

#display the data from database on terminal
def displayData():
    c.execute("SELECT * FROM Customers")
    for row in c.fetchall():
        print(row)

#copying data from database to a text file
def copyData():
    sObject = Singleton()
    dataCount = 1

    c.execute("SELECT * FROM Customers")
    with open('SOFTWAREPython\customerData.txt', 'w') as f:
        for row in c.fetchall():
            sObject.name,sObject.age,sObject.city = row[0],row[1],row[2]
            sObject = Singleton()
            f.write(f"Data {dataCount}\nName : {sObject.name}\nAge : {sObject.age}\nCity : {sObject.city}\n------------------------------\n")
            dataCount += 1


#singleton proof works without error throwing
# p = Singleton()
# p.name = "John"
# p2 = Singleton()
# print(p2.name)