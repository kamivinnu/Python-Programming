import time
from functools import wraps

# t1 = time.time()
# print("this is line one")

# x = 10
# if x >= 10:
#     print("x is equal to ten")
# print("this is line 2")

# t2 = time.time()

# print(t2 - t1)

def calculate_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"executing ....{function.__name__}")
        t1 = time.time()
        returned_value = function(*args, **kwargs)
        t2 = time.time()
        total = t2 - t1
        print(f"this funct tool loads in {total} seconds")
        return returned_value
    return wrapper


@calculate_time
def square(n):
    for i in range(1, n+1):
        print(i)


square(100)