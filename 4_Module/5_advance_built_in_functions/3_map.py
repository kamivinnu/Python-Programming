def square(n):
    e = []
    for i in n:
        e.append(i ** 2)
    return e

l = [1, 3, 5, 10]

# print(square(l))

# def square(n):
#     return n ** 3

m = list(map(lambda a : -a, l))
print(m)

lc = [-a for a in l]

