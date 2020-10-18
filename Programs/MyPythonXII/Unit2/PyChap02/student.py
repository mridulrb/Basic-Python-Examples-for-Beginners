# File name: ...\\MyPythonXII\Unit2\PyChap02\student.py
class Student:
    def __init__(self):
        print ("Enter student data...")
        self.Admno = int(input("Enter admission no.: "))
        self.Sname = input("Enter name: ")
        self.Sclass = input("Enter class: ")
        self.EngM = int(input("Enter english marks: "))
        self.PhyM = int(input("Enter physics marks: "))
        self.ChemM = int(input("Enter chemistry marks: "))
        self.MathM = int(input("Enter maths marks: "))
        self.CompM = int(input("Enter computer marks: "))
    def Student_Calc(self):
        Total = self.EngM + self.PhyM + self.ChemM + self.MathM + self.CompM
        Per = Total / 5
        Grade = self.Grade_Calc(Per)
        print ("Total marks:", Total)
        print ("Percentage of marks: %.2f" % Per)
        print ("Grade:", Grade)
    def Grade_Calc(self, Per):
        # Grade calculation condition
        if Per >= 90:
            Grade = 'A+'
        elif Per >= 80 and Per < 90:
            Grade = 'A'
        elif Per >= 70 and Per < 80:
            Grade = 'B'
        elif Per >= 60 and Per < 70:
            Grade = 'C'
        elif Per >= 50 and Per < 60:
            Grade = 'D'
        elif Per >= 40 and Per < 50:
            Grade = 'E'
        elif Per < 40:
            Grade = 'F'
        return Grade       
    def Student_Show(self):
        print ("Student details....")
        print("Admission number:", self.Admno)
        print("Name:", self.Sname)
        print("Class:", self.Sclass)
        print("English marks:", self.EngM)
        print("Physics marks:", self.PhyM)
        print("Chemistry marks:", self.ChemM)
        print("Maths marks:", self.MathM)
        print("Computer marks:", self.CompM)
        self.Student_Calc()
        
Std = Student()
Std.Student_Show()
        			
