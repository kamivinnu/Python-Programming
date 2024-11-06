

# decorators - extra functionality
# it will enhance the functionality of other function

def decorator_function(any_function):
    def wrapper_function():
        print("this is with makeup")
        any_function()
    return wrapper_function

@decorator_function
def func1():
    print("this is without makeup")

@decorator_function
def func2():
    print("this is function 2")

func2()