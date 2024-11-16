# operator overloading
# polymorphism 
# dunder methods/ magic methods (__init__)

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_full_name(self):
        return f"{self.brand} {self.model}"
    
class SmartPhone(Phone):
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera = camera

    def phone_full_name(self):
        return f"{self.brand} {self.model} {self.camera}"




my_phone = Phone("Nokia", "1100", 1000)
smart = SmartPhone("apple", "15", 150000, "12 MP")

print(smart.phone_full_name())


