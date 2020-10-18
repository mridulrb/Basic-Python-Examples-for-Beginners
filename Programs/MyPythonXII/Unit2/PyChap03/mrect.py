# File name: ...\\MyPythonXII\Unit2\PyChap03\mrect.py

# Area base class or super class
class Area:
    def Area_Calc(self, l, b):
        return l*b

# Perimeter base class or super class
class Perimeter:
    def Peri_Calc(self, l, b):
        return 2*(l+b)

# Rectangle class is derived from classes Area and Perimeter.
class Rectangle(Area, Perimeter):
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    def get_data(self):
        self.length = float(input("Enter length: "))
        self.breadth = float(input("Enter breadth: "))
        
        area = Area.Area_Calc(self, self.length, self.breadth)
        perimeter = Perimeter.Peri_Calc(self, self.length, self.breadth)
        return area, perimeter

# Main program
AP = Rectangle(0, 0)
area, perimeter = AP.get_data()
print("Area =", area)
print("Perimeter =", perimeter)
