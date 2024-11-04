# ** - kwargs

# keyword arguments - dictionary

def func(key1, **kwargs):
    print(kwargs)
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f"{k} : {v}")

d = {'name': "LinkedIN", "age": 2012, "Employer": "New_Recruit"}

# func(name = "LinkedIN", age =  2012, Employer = "New_Recruit")

func(10, **d)