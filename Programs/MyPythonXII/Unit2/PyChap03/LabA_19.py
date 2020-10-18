# File name: ...\\MyPythonXII\Unit2\PyChap03\LabA_19.py
# Base class
empArray = list() # An empty list to store employee details
class Employee:
    def __init__(self, ecode, ename, edesig):
    	self.empcode = ecode
    	self.empname = ename
    	self.empdesig = edesig
    def Emp_inputData(self):
        self.empcode = input("Enter code: ")
        self.empname = input("Enter name: ")
        self.empdesig = input("Enter desig: ")
        self.empdesig = self.empdesig.upper()
    def Emp_Display(self):
        print("Employee code:", self.empcode)
        print("Employee name:", self.empname)
        print("Employee desig:", self.empdesig)
# Derived class
class Salary(Employee):
    def __init__(self, ecode, ename, edesig):
        self.BasicSalary = 0
        self.Da = 0
        self.Hra = 0
        self.Benefit = 0
        self.Gross = 0
        Employee.__init__(self, ecode, ename, edesig)
    # Da calculation method
    def Emp_CalcDA(self):
        self.Da = self.BasicSalary * 0.8
        return self.Da
    # Hra calculation method
    def Emp_CalcHRA(self):
        self.Hra = self.BasicSalary * 0.1
        return self.Hra
    # Benefit calculation method
    def Emp_Benefit(self):
        empbenefit = 0
        if self.empdesig == 'CLERK':
            empbenefit = self.BasicSalary * 0.03
        elif self.empdesig == 'SUPERVISOR':
            empbenefit = self.BasicSalary * 0.07
        elif self.empdesig == 'MANAGER':
            empbenefit = self.BasicSalary * 0.12
        elif self.empdesig == 'SR. MANAGER':
            empbenefit = self.BasicSalary * 0.18
        elif self.empdesig == 'DIRECTOR':
            empbenefit = self.BasicSalary * 0.25        
        return empbenefit
    # Gross calculation method
    def Emp_CalcGROSS(self):
        # Accessing attributes and methods in class method
        # Calling public method through reference
        self.Da = self.Emp_CalcDA()
        self.Hra = self.Emp_CalcHRA()
        self.Benefit = self.Emp_Benefit()
        self.Gross = self.BasicSalary + self.Da + self.Hra + self.Benefit        

    def Emp_Salary(self):
        Employee.Emp_inputData(self)
        self.BasicSalary = float(input("Enter basic salary: "))
        self.Emp_CalcGROSS()
        Emp = (self.empcode, self.empname, self.empdesig, self.BasicSalary,\
               self.Da, self.Hra, self.Benefit, self.Gross)
        empArray.append(Emp) # Appends employee details into an array

# A general function to print employee details
def printEmployee(empArray):
    print(" " * 35, "Employee Details")
    print(" " * 35, "==================")
    print ("{0:^7} {1:<7} {2:<15} {3:<13} {4:>10} {5:>10} {6:>10} {7:>10} {8:>10}"
           .format("Sl.No", "Code", "Name", "Designation", "Salary", "DA", "HRA", "Benefits", "Gross"))
    print ("-" * 100)
    slno = 1
    for i in range(len(empArray)):
        ecode, ename, edesig, eBasic, eDa, eHra, eBenefit, eGross = empArray[i]
        print ("{0:^7} {1:<7} {2:<15} {3:<13} {4:>10} {5:>10} {6:>10} {7:>10} {8:>10}"
               .format(slno, ecode, ename, edesig, eBasic, eDa, eHra, eBenefit, eGross))
        slno += 1
    print ("-" * 100)
        
# Main program
S = Salary(' ', ' ', ' ')
print ("Employee salary calculation...")
ctr = 1
Ch = 'Y'
while Ch == 'Y' or Ch == 'y'or Ch == 'Yes':
    S.Emp_Salary()
    print()
    print ("Do you want to add more...<y/n>: ", end="")
    Ch = input()
    if Ch == 'N' or Ch == 'n' or Ch == 'No' or Ch == 'NO':
        break
    else:
        ctr += 1
    
printEmployee(empArray)
