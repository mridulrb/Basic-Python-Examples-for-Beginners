# File name: ...\\MyPythonXII\Unit2\PyChap02\classinitializer.py
# A simple class with initializer (constructor) method
class Student:
    # Class variables/attributes
    SRollno = 100
    SName = "Rishap Bajaj"
    SClass = 'XII-A'
    # Constructor called when creating an object of class type
    # Initializing instance attributes
    def __init__(self, sroll, sname, sclass):  
        self.SRollno = sroll
        self.SName = sname
        self.SClass = sclass        
    # A class method access instance attributes
    def Show_Student(self):
        # Accessing instance attributes in class method
        print("Student roll no.:", self.SRollno)
        print("Student name:", self.SName)
        print("Student class:", self.SClass)
    # A class method access class attributes
    def Show_ClassAttribute(self):
        print("Student roll no.:", Student.SRollno)
        print("Student name:", Student.SName)
        print("Student class:", Student.SClass)        

# Creating a class object with three parameterized values
Std1 = Student(101, 'Sandeep Nagpal', 'XII-B') # Create a new student
# Calling the class method using class instance object
Std1.Show_Student()

# Accesing class instance attributes through class object
print("Student roll no.:", Std1.SRollno) 
print("Student name:", Std1.SName)
print("Student class:", Std1.SClass)
# Accessing class attributtes inside a class method through class object
Std1.Show_ClassAttribute()

