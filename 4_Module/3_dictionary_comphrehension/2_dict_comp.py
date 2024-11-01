# dict comp with if else
# 1 : "odd", 2: "even"


def odd_even(n):
    d = {}
    for i in n:
        if n[i] > 0:
            if i % 2 == 0:
                d[i] = "Even"
            else:
                d[i] = "Odd"
    return d

d = {i : "Even" if i % 2 == 0 else "Odd" for i in list(range(1, 15))}
print(d)