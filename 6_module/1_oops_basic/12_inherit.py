# single, multilevel inheritance, multiple inheritance

# house, street, area, village, mandal, district, state

class A:
    def house(self):
        return "100"
    def hello(self):
        return "lenin nagar"
    
class B:
    def area(self):
        return "srinivas nagar"
    def hello(self):
        return "gajularamaram"
    
class C(A, B):
    def mandal(self):
        return "Qutubullapur"
    def district(self):
        return "Medchal"
    
instance_c = C()
instance_a = A()
instance_b = B()
# print(help(instance_c))
print(instance_c.__mro__())
print(instance_c.hello())