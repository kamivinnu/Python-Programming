# 1. class method vs instance method
# class method as a constructor


class Person:

    count_instance = 0
    def __init__(self, first_name, last_name, age):

        Person.count_instance += 1

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def class_constructor(cls, string):
        first, last, age = string.split(',')
        return cls(first, last, age)

    # @classmethod
    def count(cls):
        return f"you have created {cls.count_instance} instances"


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age > 18
    

p1 = Person("Bhargav", "Ram", 9)
p2 = Person("Raghu", "Thata", 2024)

print(Person.count())


# c1 = Person.class_constructor("india", "bharat" , "army")