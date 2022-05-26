# def shout(word):
#     return word.upper() + '!!!'

# print(shout('hello'))

# yell = shout
# print(yell('hello'))


###############################################################################

# def shout(text):
#     return text.upper() + '!!!'

# def whisper(text):
#     return text.lower() + '...'

# def greet(func, text):
#     greeting = func(text)
#     print(greeting)


# greet(shout, 'hello')
# greet(whisper, 'bye')

###############################################################################
#decorators


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hi():
#     print("Hi, how are you?")

# say_hi()

###############################################################################

# def add_five(func):
#     def wrapper(*args):
#         result = func(*args)
#         return result + 5
#     return wrapper

# @add_five
# def sum_two(a, b):
#     c = a + b
#     return c

# print(sum_two(2, 3))
###############################################################################
# from time import sleep

# def joke_decorator(func):
#     def wrapper():
#         print('When clock stops you all gonna die!!!!')
#         func()
#         print('Just joking I am not going to blow the earth! :) ')
#         func()
#     return wrapper

# @joke_decorator
# def countdown():
#     n = 5
#     while n > 0:
#         print(n)
#         n -= 1
#         sleep(1)
    
# countdown()

###############################################################################
# def fifty_years(func):
#     def wrapper(*args):
#         name,age = args
#         func(name, age)
#         agevalue = age + 50
#         if agevalue > 90:
#             print('die')
#         else:
#             print('alive')
#     return wrapper    
# @fifty_years
# def name(name,age):
#     print(f'hi {name}.your age is {age}')
# name("john",45)

###############################################################################
# listA = [1,2,3,4,5]
# a,b,c = listA[1:4]
# print(a,b,c)

# dicA = {'name':'john','age':45,'city':'bangalore'}
# name,age,city = dicA.values()
# print(name,age,city)

# lisA = [("john",45),("jane",34),("jack",23)]
# p1,p2,p3 = lisA
# print(p1,p2,p3)

# odev 1 = bir text gonder fonksiyona ve decorator yardimi ile onu bold , italic ve underline yap giris > hello > <b><i><u>hello</u></i></b>
# odev 2 = bir text gonder ve decoratorde onun uzunlugunu kontrol et, eger karakter sayisi 10 dan az ise yeni bir text iste ve onu buyuk harflerle yazdir
# 10 kisi yarat ve onlari variablelara list compherisonu kullanarak ata.

#bir program yaz , kahramanin adini ve classini ver , classlar mage (degnek kullaniyor), warrior (kilic), archer (ok) silahlarin farkli gucleri 
# karsinina bir canavar koy random en az 3 farkli canavar yarat. turn based combat yap. karakter olurse oyun bitsin , kazanirsa bir sonraki rounda gecsin