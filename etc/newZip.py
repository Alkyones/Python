#new zip operator
# list1 = ['name','age','school']
# list2 = ['ata',23,'KhPI']

# new_list = dict(zip(list1,list2))
# print(new_list)

# example_list = [1,2,3,4,5,6,7,8,9]
# example_list2 = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i']
# new_list = []
# for i in range(len(example_list)):
#     new_list.append((example_list[i],example_list2[i]))
# print(new_list)

# new_op = zip(example_list,example_list2)
# print(*new_op)

# # or

# new_op = dict(zip(example_list,example_list2))
# print(new_op)
# print(new_op[3])

# map function

#example_list = [1,2,3,4,5,6,7,8,9,10]
#old method
# new_list =[]

# for element in example_list:
#     new_list.append(element+3)

# print(new_list)

#what goes on here using lambda function to get a new value and assigning it to new list multiplyby5  lambda getting numbers from example list and
# new_list = list(map(lambda x : x + 3,example_list))
# print(new_list)

# user can also use ready built-in function to get a new value

# def get_new_value(number):
#     return number * 5

# example_list = list(map(get_new_value,example_list))
# print(example_list)


# list of characters of passed arguments as a new_list
# def conc(val1, val2):
#     return [val1, val2]


# old_string = ['ata', 'fearas', 'wivwi']
# old_string2 = ['ata', 'fea21r', '2121dsa']
# new_list_char = list(map(conc, old_string, old_string2))
# new_list_char2 = list(zip(old_string,old_string2))

# print(new_list_char,new_list_char2)




#conversion tuple to list

#list1 = [1,2,3,4,5]

#list2 = [1,2,3,4,5]

#new_list = list(zip(list1,list2))
#def con_list(element): return list(element)
#new_list = list(map(lambda x: list(x),new_list))
# for i in range (len(new_list)):
#     if type(new_list[i]) == tuple:
#         new_list[i] = list(new_list[i])
        
#print(new_list)#


#1 - create a new program that takes user name , surname and email then attach it to a dictionary.

#2 - yazdigin programa 3 girdi ekle(hard code) ve onu bir dict listesine donustur


# def createUser(index):
#     name = input("Name : ")
#     surname = input("Surname : ")
#     age = input("Age : ")

#     _dict = {'Index':index,'Name':name, 'Surname':surname, 'Age':age}
#     return _dict

# _peopleIndex = [1,2,3]
# _peopleIndex  = list(map(createUser,_peopleIndex))
# print(_peopleIndex)