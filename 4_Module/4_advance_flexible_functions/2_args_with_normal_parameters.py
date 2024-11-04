# *args with normal parameters

def multiply_nums(num1, num2, num3, *args):
    print(args)
    print(type(args))
    multi = 1
    for i in args:
        multi *= i
    return multi

print(multiply_nums(1, 2, 3, 4))