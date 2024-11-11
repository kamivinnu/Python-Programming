# instance methods

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self, check):
        return f"{self.first_name} {self.last_name} {check}"

p1 = Person("Bhargav", "Ram", 99)
p2 = Person("Raghu", "Thata", 2024)

print(p1.full_name(8))

print(Person.full_name(p2, 80))

l = [1, 2, 3]

l.append(5)

list.append(l, 10)

print(l)