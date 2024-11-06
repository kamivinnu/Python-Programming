

def square(n):
    ''' closure property'''
    return n ** 2

def outer():
    print("it is outer function")
    def inner():
        print("it is inner func")
    return inner

# f = outer()

# print(f())



def power(x):
    def calc_power(y):
        return y ** x
    return calc_power

cube = power(3)
square = power(2)

print(square(10))

