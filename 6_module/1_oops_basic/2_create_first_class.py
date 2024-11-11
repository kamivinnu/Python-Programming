# objectives

# what is class? 
# class is a blueprint of objects and methods

# how to create an class? class keyword
# what is init method? 
# what are attributes, instance variables
# how to create our objects/ instances?



# 1. function define inside the class is called method
# 2. class define - always first letter capital
# 3. class is a blueprint of objects and methods


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person("Bhargav", "Ram", 99)
p2 = Person("Raghu", "Thata", 2024)
print(p1)

