# MRO - method resolution order


class Phone:
    # def __init__(self, brand_name, model_name, price):
    #     self.brand_name = brand_name
    #     self.model_name = model_name
    #     self.price = price

    def make_a_call(self, phone_number):
        return (f"calling .. {phone_number}")

    def full_name(self):
        return f"{self.brand_name} {self.model_name}"
    
class Smart_phone(Phone):
    def __init__(self, brand_name, model_name, price, ram, internal_memory, rear_camera):
#         # Phone.__init__(self, brand_name, model_name, price)
        # super().__init__(brand_name, model_name, price)
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def make_a_call(self, phone_number):
        return (f"calling .. {phone_number}")

    # def full_name(self):
    #     return f"{self.brand_name} {self.model_name}"

# p1 = Phone("samsung", "guru", 11000)
# p2 = Phone("Nokia", "A1", 9000)
# p3 = Phone("Motorola", "M5", 8000)

# s1 = Smart_phone("Samsung", "S24+", 110000, "16GB", "512GB", "108MP")
# s2 = Smart_phone("Apple", "15", 180000, "12GB", "256GB", "32MP")
# s3 = Smart_phone("Motorola", "M35", 35000, "8GB", "256GB", "48MP")

print(p1.make_a_call(108))
print(s1.make_a_call(100))

print(help(Smart_phone))

# class real_me --- parent class

# class narzo (real_me) 

# class GT (real_me)

# class 