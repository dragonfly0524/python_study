class Shape():
        def __init__(self,width,len):
                self.width = width
                self.len = len
        def what_am_i(self):
                print("I am a shape")

class Rectangle(Shape):
        def __init__(self,width,len):
                self.width = width
                self.len = len
        def calculate_perimeter(self):
                return self.width * 2 + self.len * 2
        
class Square(Shape):
        def __init__(self,side):
                self.side = side
        def calculate_perimeter(self):
                return self.side * 4 
        def change_size(self,plus):
                self.side += plus

recA = Rectangle(10,20)
squA = Square(100)
print(recA.calculate_perimeter())
print(squA.side)
print(squA.calculate_perimeter())
squA.change_size(40)
print(squA.side)
recA.what_am_i()
squA.what_am_i()

class Horse():
        def __init__(self,name,bleed,rider):
                self.name = name
                self.bleed = bleed
                self.rider = rider

class Rider():
        def __init__(self,name):
                self.name = name

take = Rider("Take Yutaka")
deep = Horse("Deep Impact","sala",take)
print(deep.rider.name)
