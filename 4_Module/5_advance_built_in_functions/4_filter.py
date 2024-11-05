# filter function

# def even(n):
#     e = []
#     for i in n:
#         if i % 2 == 0:
#             e.append(i)
#     return e
    
l = list(range(1, 11))

# print(even(l))

def even_filter(n):
    return n % 2 == 0

ft = list(filter(lambda d : d % 2 != 0, l))

# print(ft)

# task : same thing do in lc

lc = [i for i in l if i % 2 == 0]

print(lc)