class Square:
        squs = []
        
        def __init__(self,w1,w2,w3,w4):
                self.width1 = w1
                self.width2 = w2
                self.width3 = w3
                self.width4 = w4
                self.squs.append((self.width1,self.width2,self.width3,self.width4))

        def print_size(self):
                print("{} by {} by {} by {}".format(self.width1,self.width2,self.width3,self.width4))

s2 = Square(50,60,70,80)

s2.print_size()


def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "b"))
