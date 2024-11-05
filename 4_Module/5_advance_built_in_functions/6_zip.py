a = ["High", "Junior", "Railway", "Police"]

b = ["school", "college", "line", "station"]

# print(list(zip(a, b))) # try to do in dict

# define a function that takes any no. of list containing numbers
# [1,2,3],[4,5,6],[7,8,9]
# return average
# (1+4+7)/3, (2+5+8)/3 , (3+6+9)/3

# try to make this anonymous function in one line using lambda 
# expression


def avg_finder(l1, l2, l3):
    e = []
    for i in zip(l1, l2, l3):
        e.append(sum(i)/len(i))
    return e

print(avg_finder([1, 2, 3], [4, 5, 6], [7, 8, 9])) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

