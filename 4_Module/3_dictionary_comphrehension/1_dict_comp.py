
# cat - one file
# touch - n no. of files


# square { key : value ** 2}

def dict_square(n):
    d = {}
    for i in n:
        d[i] = i ** 2
    return d

def word_count(n):
    d = {}
    for i in n:
        d[i] = n.count(i)
    return d

c = "Indian      ArmyIndian      Army"

# print({i : c.count(i) for i in c})


