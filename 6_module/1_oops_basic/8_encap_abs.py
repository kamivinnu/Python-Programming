# encapsulation,

# abstruction

# some special naming conventions

# name mangling(__name) 

# access modifiers = public, private, protected

class Phone:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.__price = price

    def make_a_call(self, phone_number):
        return (f"calling .. {phone_number}")

    def full_name(self):
        return f"{self.brand_name} {self.model_name}"
    


p1 = Phone("Samsung", "S24", 10000)

print(p1._Phone__price)

print(p1.__dict__)

p1._Phone__price = 12000

print(p1._Phone__price)


