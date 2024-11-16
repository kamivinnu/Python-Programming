class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = max(price, 0)
        # if price > 0:
        #     self.price = price
        # else:
        #     self.price = 0

    @property
    def complete_spec(self):
        return f"{self.brand} {self.model} and the price is {self.price}"

    # getter(), setter()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)

    def make_a_call(self, phone_number):
        return (f"calling .. {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model}"
    
p1 = Phone("Nokia", "A1", 1000)

p1.price = 500

print(p1.price)

print(p1.complete_spec)

