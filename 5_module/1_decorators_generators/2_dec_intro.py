
from functools import wraps
# decorators - extra functionality
# it will enhance the functionality of other function

def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        print("this is with makeup")
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def func1():
    print("this is without makeup")

@decorator_function
def add(a, b):
    ''' this is add function '''
    return a + b

print(add.__doc__)
print(add.__name__)


# let = decorator_function(func1)

# let()
