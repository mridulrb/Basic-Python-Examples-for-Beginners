# File name: ...\\MyPythonXII\Unit2\PyChap03\LabA_20.py
# Person base class or super class
class Person:
    def __init__(self, name, age, psex):
    	self.pname = name
    	self.paga = age
    	self.psex = psex
    def Person_inputData(self):
        print ("Person's information....")
        print ("==========================")
        self.pname = input("Enter name: ")
        self.page = int(input("Enter age: "))
        self.psex = input("Enter gender: ")    
    def Person_Display(self):
        print()
        print ("Teacher detail is:")
        print ("==========================")
        print("Name:", self.pname)
        print("Age:", self.page)
        print("Sex:", self.psex)

# Employee base class or super class
class Employee:
    def __init__(self, ecode, edesig, esalary):
    	self.empcode = ecode
    	self.empdesig = edesig
    	self.empsalary = esalary
    def Emp_inputData(self):
        self.empcode = input("Enter code: ")
        self.empdesig = input("Enter designation: ")
        self.empsalary = input("Enter basic salary: ")    
    def Emp_Display(self):
        print("Code:", self.empcode)
        print("Designation:", self.empdesig)
        print("Salary:", self.empsalary)

# Derived class for multiple inheritance
class Teacher(Person, Employee):
    def __init__(self, a, b, c, d, e, f):
        # Invoking base class constructors
        Person.__init__(self, a, b, c)
        Employee.__init__(self, d, e, f)
    def get_data(self):
        # Invoking base class methods
        Person.Person_inputData(self)
        Employee.Emp_inputData(self)        
    def show_data(self):
        # Invoking base class methods
        Person.Person_Display(self)
        Employee.Emp_Display(self)

# Main program
T = Teacher(' ', 0, ' ', ' ', ' ', 0)
T.get_data()
T.show_data()
