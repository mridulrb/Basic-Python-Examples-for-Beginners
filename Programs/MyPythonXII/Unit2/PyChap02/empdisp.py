# File name: ...\\MyPythonXII\Unit1\PyChap02\empdisp.py
# Accessing employee information using class
class Employee:
    # Class variables
    empcode = ""
    empname = ""
    empdesig = ""
    empbasic = 0
    # Constructor called when creating an object of class type
    def __init__(self, ecode, ename, edesig, esal):  
        self.empcode = ecode
        self.empname = ename
        self.empdesig = edesig
        self.empbasic = esal
    # A class method
    def Display(self):
        # Accessing attributes in class method
        print ("Here is the employee information....")
        print ("=" * 30)
        print("Employee code:", self.empcode)
        print("Employee name:", self.empname)
        print("Employee designation:", self.empdesig)
        print("Employee salary:", self.empbasic)
# Creating a class object with three parameterized values
Emp = Employee("E100", 'Mr. B Srinivasan', 'Sr. Programmer', 12600) 
# Calling the class method using instance object
Emp.Display()

