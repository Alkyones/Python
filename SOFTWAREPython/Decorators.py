#example 2 
import time

def timed(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        after = time.time()
        print(f"{func.__name__} took {after - before} seconds")
        return value
    return wrapper

@timed
def my_function(x):
    result = 1
    for i in range(1,x) :
         result *= i
    return result


my_function(20220)