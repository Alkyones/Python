#sinirsiz sekilde random veri uretimi

#import faker - pip install Faker
from faker import Faker


person = Faker()
#print(person.name())
#manual person
person0 = 'Joe'
person1 = 'Sinem'
person2 = 'Sara'
person3 = 'Seyma'
person4 = 'Ayse'
#print(person0, person1, person2, person3, person4)
#task 100 tane isim olustur ver bana.
for i in range(10): #100
    print(person.name(),person.city())
    print()

#https://faker.readthedocs.io/en/master/