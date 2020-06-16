import math

class Circle():
        def __init__(self, radius):
                self.radius = radius

        def cal_area(self):
                return self.radius **2 * math.pi

circle1 = Circle(10)
print(circle1.cal_area())

class  Triangle():
        def __init__(self,bottom,height):
                self.bottom = bottom
                self.height = height
                
        def calculate_area(self):
                return self.bottom * self.height / 2

triA = Triangle(10,20)
print(triA.calculate_area())

class Hexagon():
        def __init__ (self,side):
                self.side = side
        def calculate_perimeter(self):
                return self.side * 6
hexaA = Hexagon(7)
print(hexaA.calculate_perimeter())
333
