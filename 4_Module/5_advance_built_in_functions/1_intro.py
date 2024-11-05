# lambda expression 
# lambda - anonymous function

def add(a, b):
    return a + b

# print(add(1, 4))

# l = lambda a, b: (a + b)

# print(l(5, 8))



def is_even(a):
    if a%2 == 0:
        return True
    else:
        return False

# print(is_even(3))

check = lambda a : a % 2 == 0
# print(check(9))


def last(d):
    return d[-1]

last_char = lambda a : a[::-1]
# print(last_char("kalyani"))\

def func(s):
    if len(s) > 5:
        return True
    return False

length = lambda y : len(y) > 5

print(length("python"))