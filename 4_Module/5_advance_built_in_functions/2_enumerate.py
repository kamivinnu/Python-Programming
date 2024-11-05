# "India" 
# 0 ---- I
# 1 ---- n
# 2 ---- d

name = "World"

# pos = 0
# for i in name:
#     print(f"{pos} -- {i}")
#     pos += 1


# for p, v in enumerate(name):
#     print(f"{p} : {v}")


# define a function that takes two arguments
# 1- list containing string
# 2- string that want to find in your list
# and this function will return the index of string in your list and
# if string is not present then return -1

l = ["apple", "glass", "pencil", "water"]

def find_pos(li, target):
    for p, v in enumerate(li):
        if v == target:
            return p
    return -1
    
print(find_pos(l, "water"))