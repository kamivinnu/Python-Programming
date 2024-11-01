# flexible functions - *---args, ** --- kwargs 

def square(*n):
    l = []
    for i in n:
        l.append(i**2)
    return l

print(square(1, 2, 3))