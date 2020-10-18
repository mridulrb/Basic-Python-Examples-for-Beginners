# File name: ...\\MyPythonXII\Unit2\PyChap02\sclass.py
# A simple class
class Student:
    # Class variables/attributes
    SRollno = 100
    SName = "Rishap Bajaj"
    SClass = 'XII-A'

#Access class variable
print ("The class variables are: ", Student.SRollno, Student.SName, Student.SClass, sep=" ")

# Creating a class object
Std1 = Student()
# Accessing class variables through class object variable
print ("The object variables are: ", Std1.SRollno, Std1.SName, Std1.SClass, sep=" ")
