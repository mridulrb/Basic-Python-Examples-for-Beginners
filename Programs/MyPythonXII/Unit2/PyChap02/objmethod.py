# File name: ...\\MyPythonXII\Unit2\PyChap02\objmethod.py
# A simple with class method
class Student:
    SnRollno = 100
    SnName = "Rishap Bajaj"
    SnClass = 'XII-A'
    # A class method
    def Show_Student(self):
        print("Student roll no.:", self.SRollno)
        print("Student name:", self.SName)
        print("Student class:", self.SClass)

Student().Show_Student() # Calling class method
# Creates a class object
Std1 = Student()
# Calling the class method using instance object
Std1.Show_Student()
