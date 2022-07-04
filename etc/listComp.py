#first example 

fruits = ['apples', 'banana', 'strawberry']

#looping through the list
for fruit in fruits:
    print(fruit)

#with list compherisonu
[ print(fruit) for fruit in fruits]


#changing the first letters

#with loop
# new_fruit_list = []

# for fruit in fruits:
#     new_fruit_list.append(fruit.capitalize())
# print(new_fruit_list)

# #with list compherison
# fruits = [fruit.capitalize() for fruit in fruits]
# print(fruits)
from random import choice
bits = [choice([True, False]) for i in range(10)]
bits = ['0' if bit == True else '1' for bit in bits]
print(bits)


#string manipulation
string = 'HelloThisIsAString'
string = "".join(
    [ char if char.islower() else " " + char for char in string]
)

print(string.lstrip())