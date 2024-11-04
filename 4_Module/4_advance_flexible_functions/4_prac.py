# define a function
# input
# num , iterable(tuple, list) containing number as args

# example
# nums = [1,2,3]
# to_do(3 , *num)

# output
# list - [1**3, 8 ,27]

# if user didn't pass any args then give a msg as 'hey u didn't pass'
# args
# 
# else
# return list
# 
# note - use list comphrehension
# 


def to_do(n, *args):
    l = []
    for i in args:
        l.append(i**n)
    return l

l = [1, 2, 3, 4]
print(to_do(4, *l))

n = 4
print([i**n for i in l])