# import math
# result_list = []


# def inputHandler(x_value):
#     try:
#         float(x_value)
#         return float(x_value)
#     except:
#         print('Invalid x value')

# while True:
#     x_value = inputHandler(input('Enter the x value : '))
#     if x_value <0:
#      res_val = 2-x_value
#     elif 0<= x_value <= 2.5:
#         abs_value = abs(1-x_value)
#         if abs_value != 0:
#             res_val = 1 - (3*math.log(abs(1-x_value)))
#         else:
#             print('Log 0 is undefined.')
#     else:
#         res_val= math.sin((2.3)*x_value)-1 #python sin method can handle radians, numbers and floats

#     result_list.append(res_val)
#     print('Saved results : ' , result_list)
#     conti_val = input('Do you want to continue ? (y/n)')
#     if conti_val == 'n' : break



######################


def listSorter(list_input):
    ps_list = list(reversed(sorted([x for x in list_input if x > 0])))
    ng_list = sorted([x for x in list_input if x < 0])
    ng_list.extend(ps_list)
    return(ng_list)

def testListSorter():
    #assert listSorter([1,7,2,-2,1])==[-2, 0,1,2,7],'List not matching'
    #assert listSorter([1,7,2,-2,1])==[-2, 1,1,2,7],'Function is working correctly'
    pass


testListSorter()