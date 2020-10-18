# File name: ...\\MyPythonXII\Unit2\PyChap02\Emp.py
class Employee:
    emp_no = 0
    emp_name = " "
    emp_add = " "
    emp_dept = " "
    def read_employee(self):
        print ("Enter employee details....")
        self.emp_no = int(input("Enter number: "))
        self.emp_name = input("Enter name: ")
        self.emp_add = input("Enter address: ")
        self.emp_dept = input("Enter department: ")
    def display_employee(self):
        print ("Employee details....")
        print("Number:", self.emp_no)
        print("Name:", self.emp_name)
        print("Addres:", self.emp_add)
        print("Department:", self.emp_dept)
emp = Employee()
emp.read_employee()
emp.display_employee()
        			
