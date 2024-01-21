# side effect on the mutable variable
# def theLargestNumber(nums, n):
#     nums.sort(reverse = True)
#     return nums[:n]

# randList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(randList)
# print(theLargestNumber(randList, 3))
# print(randList)

#! list comprehensions
# x = [i for i in range(10)]
# x = [[j for j in range(10)] for i in range(10)]
# print(x)

#! arguments passing
def example_def(a,b=None,y=None):
    print(a,b,y)
    
example_def(a=1,y=2)
