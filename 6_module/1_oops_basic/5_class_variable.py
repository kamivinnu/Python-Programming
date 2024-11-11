

class Circle:
    pi = 3.14
    count_instance = 0

    def __init__(self, radius):
        Circle.count_instance += 1
        self.radius = radius
        # self.pi = pi

    def calc_cirumcumference(self):
        return 2*Circle.pi*self.radius
    
c1 = Circle(6)
c2 = Circle(10)
c3 = Circle(100)

print(c2.calc_cirumcumference())

print(Circle.count_instance)