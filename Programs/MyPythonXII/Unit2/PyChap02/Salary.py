# File name: ...\\MyPythonXII\Unit2\PyChap02\Salary.py
class Teacher:
    TName = TAddress = TQualification = " "
    TAge = 0
    def __init__(self):
        self.TName = " "
        self.TAddress = " "
        self.TQualification = " "
        self.TAge = 0
    def Enter_Details(self):
        print ("Enter teacher data...")
        self.TName = input("Enter name: ")
        self.TAddress = input("Enter address: ")
        self.TQualification = input("Enter qualification: ")
        self.TAge = int(input("Enter age: "))
    def Calc_Sal(self, Tq, Ta):
        if Tq.upper() == "TGT":
            sal = 22100
        elif Tq.upper() == "PGT":
            sal = 32400
        else:
            sal = 16400
        if Ta > 50:
            sal = sal + sal * 0.1
        return sal            
    def Display_Details(self):
        print ("Teeacher details...")
        print("Name:", self.TName)
        print("Addres:", self.TAddress)
        print("Qualification:", self.TQualification)
        print("Age:", self.TAge)
        Tsal = self.Calc_Sal(self.TQualification, self.TAge)
        print("Salary:", Tsal)
T = Teacher()
T.Enter_Details()
T.Display_Details()

        			
