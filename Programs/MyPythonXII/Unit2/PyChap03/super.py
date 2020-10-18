# File name: ...\\MyPythonXII\Unit2\PyChap03\super.py
# Base class
class School:
    # Base class constructor method
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
    def MyMessage(self):    
        print ("I am in school class")
    # Base class method
    def displayInformation(self):
        print("Name:", self.Name)
        print("Age:", self.Age)
        
# Derived class
class Teacher(School):
    # Derived class constructor method
    def __init__(self, name, age, salary):
        # Invoking base class constructor method
        super(Teacher, self).__init__(name, age)    # Gets the instance of the parent object
        self.Tsalary = salary
        print("Teacher's detail....")
        # Invoking base class method
        School.displayInformation(self)
        print("Salary:", self.Tsalary)
    def MyMessage(self):    # Override method
        print ("I am a teacher in physics department")
        super(Teacher, self).MyMessage()

# Main program
Th = Teacher('Mrs. Poonam Sharma', 35, 16000)
print()
Th.MyMessage()