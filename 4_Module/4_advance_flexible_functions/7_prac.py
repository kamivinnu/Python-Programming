# Define a function,
# when we call the function, it has to give output as first letter in Capital.
# when we call the function, it has to give output in reverse of a string and 
# first capital letter.

def func(name, **kwargs):
    if (kwargs.get('reverse') == True):
        return name[::-1].title()
    else:
        return name.title()
    
print(func("india", reverse = True))