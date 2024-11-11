# create your first generator with generator function
# 1. generator function
# 2. gene comphrehension

# 10, 1 to 10

def value_print(n):
    return n ** 2
l = [5, 4, 3, 2, 1]
# print(tuple(map(lambda a : a **2, l)))



l = (i**2 for i in range(1, 11))
# print(tuple(l))


# define a generator function ------ yield keyword
# take one number as a argument
# generate a sequence of even numbers from 1 to that number


def gene(n):
    # e = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i
    
for i in gene(20):
    print(i)