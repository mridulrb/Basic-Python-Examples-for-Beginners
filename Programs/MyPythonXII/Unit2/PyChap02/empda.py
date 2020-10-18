# File name: ...\\MyPythonXII\Unit2\PyChap02\empda.py
# Accessing employee information using class
class Employee:
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
    def Calc_DA(self, esal):
        da = esal * 0.8 # Calculating da as a local variable
        return da
    # A class method
    def Display(self, esal):
        # Accessing attributes in class method
        empda = self.Calc_DA(self.empbasic) # Calling function through reference
        print ("Here is the employee information....")
        print ("=" * 30)
        print("Employee code:", self.empcode)
        print("Employee name:", self.empname)
        print("Employee designation:", self.empdesig)
        print("Employee salary:", self.empbasic)
        print("Employee DA: %.2f" % empda)
# Creating a class object with three parameterized values
Emp = Employee("E100", 'Mr. B Srinivasan', 'Sr. Programmer', 12600)
# Calling the class method using instance object
Emp.Display(Emp.empbasic)

