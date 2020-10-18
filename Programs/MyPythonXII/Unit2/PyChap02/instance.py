# File name: ...\\MyPythonXII\Unit2\PyChap02\instance.py
# A simple class with initializer (constructor) method
class Student:
    SRollno = 100
    SName = "Rishap Bajaj"
    SClass = 'XII-A'
    # Constructor called when creating an object of class type
    def __init__(self, sroll, sname, sclass):
        # Creating instance variables
        self.Nrollno = sroll
        self.Nname = sname
        self.Nclass = sclass
    # Class methods
    def Show_Class(self):
        # Printing class variables
        print("Student roll no.:", self.SRollno)
        print("Student name:", self.SName)
        print("Student class:", self.SClass)
    def Show_Instance(self):        
        # Printing instance variables
        print("Student roll no.:", self.Nrollno)
        print("Student name:", self.Nname)
        print("Student class:", self.Nclass)


# Creating a class object with three parameterized values
Std1 = Student(101, 'Sandeep Nagpal', 'XII-B') # Create a new student
# Calling the class method
print("A student as class variables")
Std1.Show_Class()  # Printing class variables values
print()
print("A student as instance variables")
Std1.Show_Instance()  # Printing instance variables values
