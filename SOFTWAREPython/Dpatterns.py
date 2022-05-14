#from abc import ABCMeta, abstractstaticmethod


# hello , today/yesterday is/was a beautiful/bad day , i am/was learning python/html , and i am/was very happy/sad

# class greeting:
#     def __init__(self, date, mood, language, feeling):
#         self.date = date
#         self.mood = mood
#         self.language = language
#         self.feeling = feeling

#     def greeter(self):
#         if self.date == "today":
#             _const = 'is'
#             _constPerson = 'am'
#         else:
#             _const = 'was '
#             _constPerson = 'was '

#         print(
#             f"Hello, {self.date} {_const} a {self.mood} day, I {_constPerson} learning {self.language} and I {_constPerson} very {self.feeling}")
       
# person1 = greeting("today", "beautiful", "python", "happy")
# person2 = greeting("yesterday", "bad", "html", "sad")
# person3 = greeting("today", "awful", "ruby", "excited")

# person1.greeter()
# person2.greeter()
# person3.greeter()

################################################################    


# class Order:
#     def __init__(self, id, ketchup, mustard, mayo, salam, tomato, pickle, onion, cheese,extra):
#         self.id = id
#         self.ketchup = ketchup
#         self.mustard = mustard
#         self.mayo = mayo
#         self.salam = salam
#         self.tomato = tomato
#         self.pickle = pickle
#         self.onion = onion
#         self.cheese = cheese
#         self.extra = extra

#     def getOrder(self):
#         print(f"Order has been received from {self.id}...")
#         print(f"Ketchup: {self.ketchup} ounce")
#         print(f"Mustard: {self.mustard} ounce")
#         print(f"Mayo: {self.mayo} ounce")
#         print(f"Salam: {self.salam} gram")
#         print(f"Tomato: {self.tomato} slices")
#         print(f"Pickle: {self.pickle} slices")
#         print(f"Onion: {self.onion} slices")
#         print(f"Cheese: {self.cheese} grams")
#         print(f"Extra: {self.extra}")


# order1 = Order("3213124", 10, 5, 0, 10, 100, 5, 5, 2, 100)
# order1.getOrder()     
# order2 = Order("3213124", 10, 5, 0, 10, 100, 5, 5, 2,'Aci sos , fazladan pismis tavuk kanatlari ve yarim litre kola')
# order2.getOrder()



################################################################
# class Order:
    
#     ####static method ###
#     def execute(self):
#         print("Order has been received...")

    
    
# class getOrderPizza(Order):
#         pass


# class getOrderBurger(Order):
#         pass

# class getOrderSandwich(Order):
#         pass

################################################################
#1- Create a builder which takes order of creating a house ( rooms , doors , windows , etc..) and returns a house ( in print statements )
#2- Create a builder which takes order of creating a car ( wheels , doors , etc..) and returns a car ( in print statements )
#3- Create a builder which creates a student (disciplines, etc..) and returns a student pass grade ( in print statements )





