# File name: ...\\MyPythonXII\Unit2\PyChap03\polygon.py
# Demonstrating the class inheritance
class Polygon:
    ht = 0
    wt = 0
    def __init__(self, height, width):
        self.ht = height
        self.wt = width    

class Rectangle(Polygon):
    def __init__(self, height, width):
        Polygon.__init__(self, height, width)
    def R_Area(self):
        return (self.wt * self.ht);

class Trinagle(Polygon):
    def __init__(self, height, width):
        Polygon.__init__(self, height, width)
    def T_Area(self):
        return (self.wt * self.ht / 2);
    
        
h = int(input("Enter length: "))
w = int(input("Enter height: "))
R = Rectangle(h, w)
T = Trinagle(h, w)
print("The area of rectangle:", R.R_Area())
print("The area of triangle:", T.T_Area())
