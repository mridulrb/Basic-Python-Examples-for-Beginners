# File name: ...\\MyPythonXII\Unit2\PyChap03\emang.py
# Program to read and display information of employee and manager
class Employee:
    emp_no = 0
    emp_name = ' '
    eaddress = ' '
    edept = ' '
    def emp_input(self):
        self.emp_no = int(input("Enter the Employee number: "))
        self.emp_name = input("Enter the Employee name: ")
        self.eaddress = input("Enter the Employee address: ")
        self.edept = input("Enter department: ")
    def emp_print(self):
        print("Employee number: ", self.emp_no)
        print("Address: ", self.eaddress)
        print("Employee name: ", self.emp_name)
        print("Address: ", self.eaddress)
        print("Department: ", self.edept)
# Employee inherited in manager class
class Manager(Employee):
    def Emp_input(self):
        Employee.emp_input(self)
        self.__no_of_emp = int(input("Enter number of employee under manager: "))
    def Emp_print(self):
        Employee.emp_print(self)
        print("No of employee under manager:" , self.__no_of_emp)

# Main program
M = Manager()
M.Emp_input()
M.Emp_print()
