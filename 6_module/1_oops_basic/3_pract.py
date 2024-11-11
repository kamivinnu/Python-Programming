# create a laptop class with attributes like brand name, model name, price

# create the objects/instance of your laptop class

class Laptop:
    count = 0
    discount_percent = 21
    def __init__(self, brand_name, model_name, price):
        Laptop.count += 1
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def apply_discount(self):
        off_price = (Laptop.discount_percent/100)*self.price
        return self.price - off_price
        

l1 = Laptop("Lenovo", "idea 3", 60000)
l2 = Laptop("Asus", "vivo book 15", 45000)
l3 = Laptop("Dell", "nakteliyadu", 43000)
l4 = Laptop("HP", "Victus", 99000)

print(l4.apply_discount())

print(Laptop.count)