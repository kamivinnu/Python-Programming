# func with all parameters

# PADK

# parameter
# argument
# default parameter (key = 10, key2 = 20)
# kwargs


def func_all(normal, default = 500, *args, **kwargs):
    print(default)
    print(normal)
    print(args)
    print(kwargs)

l = [12.5, 25, 50, 100]
d = {'one': 1, "two": 2}
func_all(9, *l, **d)