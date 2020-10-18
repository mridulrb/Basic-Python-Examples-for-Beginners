# File name: ...\\MyPythonXII\Unit2\PyChap02\cattribute.py
# Access class attributes
class Student:
    # Class document string
    'A Student base class for all students.'
    SRollno = 100
    SName = "Rishap Bajaj"
    SClass = 'XII-A'
    # Constructor called when creating an object of class type
    def __init__(self, sroll, sname, sclass):
        # Creating instance variables
        self.Nrollno = sroll
        self.Nname = sname
        self.Nclass = sclass
    def Show_Instance(self):        
        # Printing instance variables
        print("Student roll no.:", self.Nrollno)
        print("Student name:", self.Nname)
        print("Student class:", self.Nclass)

Std1 = Student(1, 2, 3)
print ("Class name is:", Student.__name__)
print ("Student class document string is:", Student.__doc__)
print ("Student module is:", Student.__module__)
print ("The base class:", Student.__bases__)
print ("Dictionary of Student class namespace:", Student.__dict__)
Std1.
print (vars(Std1))
