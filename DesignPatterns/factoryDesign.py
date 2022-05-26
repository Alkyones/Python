from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def person_create():
        """
        Interface
        """

#subclasslar  
class student(IPerson):
    def __init__(self, name):
        self.name = name

    def person_create(self):
        print("Student: " + self.name + " created")

class teacher(IPerson):
    def __init__(self, name):
        self.name = name

    def person_create(self):
        print("Teacher: " + self.name + " created")


stud1 = student('John')
stud1.person_create()
print(stud1.name)

# stud2 = student('Mary')
# stud2.person_create()

# teac1 = teacher('John')
# teac1.person_create()

# teac2 = teacher('Mary')
# teac2.person_create()

# factory design odev : kullanici bir dosya ismi veriyor ve icine yazilmasi gereken notu yaziyor.
# factory creator ise txt ise txt, html ise html , xml ise xml dosyasi olusturup bunu yaratiyor.