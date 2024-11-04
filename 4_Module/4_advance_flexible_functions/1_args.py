# flexible functions - *---args, ** --- kwargs 

# def square(*n):
#     l = []
#     for i in n:
#         l.append(i**2)
#     return l

# print(square(1, 2, 3))

def total(a, b):
    return a + b

# print(total(5, 10, 15, 20)) # 15


def allllll(*args):
    total = 0
    for i in args:
        total += i
    return total

print(allllll(1, 2, 3, 8, 5))

# (1), (1, )