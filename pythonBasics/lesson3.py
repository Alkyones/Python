#if for while



# a = int(input('Enter a number: '))
# b = int(input( 'Enter a number: '))


#if

# print('code will run here')
# if a == 7:
#     print('a is my lucky number 7')
    
# if a > b:
#     print('a is greater than b')
# elif a == b:
#     print('a is equal to b')
# else: 
#     print('b is greater than a')
# print('code will run here tooo')


#loop

#for

numbers = [1,2,3,4,5,6,7,8,9,10]

# for number in numbers:
    # if number %2: print('this is an odd number') or print('this is an even number')
    # break ## donguyu kir
    # if number %2:
    #     print("this is an even number")
    # else:
    #     print("this is an odd number")


#while

# total = 0
# while total != 100:
#     total += 1
#     print(total)



age = 0    
while age <= 0 or age > 120: 
    age = input('Please enter your age: ')
    if type(age) == str:
        age = int(age)
    
print('your age is', age)