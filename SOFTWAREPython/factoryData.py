# for design pattern used abc in python
from abc import ABCMeta, abstractstaticmethod
# xml parser
from xml.dom import minidom
# bat script structurer
#import struct
import sys
import sqlite3


class Singleton:
    __instance = None

    def __new__(cls):
        if Singleton.__instance is None:
            cls.__instance = \
                super(Singleton, cls).__new__(cls)
        return cls.__instance


class IData(metaclass=ABCMeta):
    @abstractstaticmethod
    def save_data():
        """Data Interface"""
    
    def __init__(self, save_path, load_path):
        self.save_path = save_path
        self.load_path = load_path
        

# class can be used to create a txt data store from db file
class txtData(IData):
    def save_data(self):
        conn = sqlite3.connect(self.load_path)
        c = conn.cursor()
        sObject = Singleton()

        print('Saving data to {}'.format(self.save_path))

        c.execute("""SELECT * FROM Customers""")
        with open(self.save_path, 'w') as f:
            f.write("This file has been created by a factory designal pattern\n")
            for row in c.fetchall():
                sObject = Singleton()
                sObject.customer_name, sObject.customer_age, sObject.customer_city = row[0], row[1], row[2]
                f.write(
                    f"Data: {sObject.customer_name}, {sObject.customer_age}, {sObject.customer_city}\n")
        conn.close()
        return "Data saved to {}".format(self.save_path)

# class can be used to create a xml file from db file
class xmlData(IData):

    def save_data(self):
        #new xml file to save data
        root = minidom.Document()
        xml = root.createElement('root')
        root.appendChild(xml)

        #connect to db file
        conn = sqlite3.connect(self.load_path)
        c = conn.cursor()
        print('Saving data to {}'.format(self.save_path))
        c.execute("""SELECT * FROM Customers""")
        for row in c.fetchall():
            #singleton object can be used to store data from db denies any conflict
            sObject = Singleton()
            sObject.customer_name, sObject.customer_age, sObject.customer_city = row[0], row[1], row[2]
            #create a new xml node
            productChild = root.createElement('customer')
            productChild.setAttribute('name', sObject.customer_name)
            productChild.setAttribute('age', str(sObject.customer_age))
            productChild.setAttribute('city', sObject.customer_city)
            xml.appendChild(productChild)
            xml_str = root.toprettyxml(indent="\t")
        #save xml file
        with open(self.save_path, "w") as f:
            f.write(xml_str)
        
        return "Data saved to {}".format(self.save_path)


# class can be used to create a bat file from db file
class batData(IData):
    

    def save_data(self):
        conn = sqlite3.connect(self.load_path)
        c = conn.cursor()

        print('Saving data to {}'.format(self.save_path))
        
        c.execute("""SELECT * FROM Customers""")
        with open(self.save_path, 'w') as f:
            f.write("@echo off\n")
            f.write("cls\n")
            f.write("echo This file has been created by a factory designal pattern\n")
            for row in c.fetchall():
                sObject = Singleton()
                sObject.customer_name, sObject.customer_age, sObject.customer_city = row[0], row[1], row[2]
                f.write(
                    f"echo Data: {sObject.customer_name}, {sObject.customer_age}, {sObject.customer_city}\n")
        conn.close()
        return "Data saved to {}".format(self.save_path)

#main class drive
class DataFactory():

    @staticmethod
    def get_method(savingMethod):
        try:
            if savingMethod == 'txt':
                return txtData('SOFTWAREPython\CustomerData.txt','SOFTWAREPython\CustomerData.db')
            elif savingMethod == 'xml':
                return xmlData('SOFTWAREPython\CustomerData.xml','SOFTWAREPython\CustomerData.db')
            elif savingMethod == 'bat':
                return batData('SOFTWAREPython\CustomerData.bat','SOFTWAREPython\CustomerData.db')
            raise AssertionError('Invalid saving method')
        except AssertionError as e:
            return print(e, '\nFactory has only bat , txt and xml methods')

#main function singleton to factory with argv
if __name__ == '__main__':
    data = DataFactory.get_method('txt')
    print(data.save_data())
