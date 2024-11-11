# generators vs iterators

# iterator vs iterable

l = [1, 2, 3] # iterable

# for i in l: 
#     print(i)

a = iter(l) # iterator
print(a)
# for i in a:
#     print(i)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# next func calls only for iterator not for iterable
# you can run for loop on iterable as well as iterator

for i in map(lambda a : a ** 2, l):
    print(i)

# generators are iterators
# generators is also a sequence

print(map(lambda a : a ** 2, l))