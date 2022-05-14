from unicodedata import name


class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value
    
    @staticmethod
    def FullPerson():
        return "hi"

    
p1 = Person('Ata',23,'Male')

print(p1.Name)
print(p1.FullPerson)