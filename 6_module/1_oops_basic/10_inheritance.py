

class Phone:
    def make_a_call(self, phone_number):
        return (f"calling .. {phone_number}")
    

class Smart:
    pass
    # def make_a_call(self, phone_number):
    #     return (f"calling .. {phone_number}")
    
# l = list(tuple(range(1, 11)))
# print(help(l))
p1 = Phone()
s1 = Smart(p1)
# print(p1.make_a_call(108))
print(s1.make_a_call(100))