# File name: ...\\MyPythonXII\Unit2\PyChap03\inher1.py
# Base class
class School:
    # Base class constructor method
    def __init__(self, name, age, address):
        self.BaseName = name
        self.BaseAge = age
        self.BaseAddress = address
    # Base class method
    def displayInformation(self):
        print("Name:", self.BaseName)
        print("Age:", self.BaseAge)
        print("Address:", self.BaseAddress)
        
# Derived class
class Teacher(School):
    # Derived class constructor method
    def __init__(self, name, age, salary, address, subject):
        # Invoking base class constructor method
        School.__init__(self, name, age, address)
        self.Tsubject = subject
        self.Tsalary = salary
        print("Teacher's detail....")
        # Invoking base class method
        School.displayInformation(self)
        print("Subject:", self.Tsubject)
        print("Salary:", self.Tsalary)
        

# Derived class
class Student(School):
    # Derived class constructor method
    def __init__(self, name, age, address, marks, fees):
        # Invoking base class constructor method
        School.__init__(self, name, age, address)
        self.Smarks = marks
        self.Sfees = fees
        print("Student's detail....")
        # Invoking base class method
        School.displayInformation(self)
        print("Marks:", self.Smarks)
        print("Fees:", self.Sfees)
        

# Main program
Th = Teacher('Mrs. Poonam Sharma', 35, 16000, 'B-45, Sec-12, Dwaraka, Delhi', "Physics")
print()
St = Student('Amit kumar', 16, 'Bu-35, Pipuram pura, Delhi', 435, 12400)
