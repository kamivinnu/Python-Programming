# *args with arguments

def multiply_nums(*args):
    print(args)
    print(type(args))
    multi = 1
    for i in args:
        multi *= i
    return multi

# to unpack the elements in argument we use * args
l = [1, 2, 3, 4]
print(multiply_nums(*l, 10, 15))