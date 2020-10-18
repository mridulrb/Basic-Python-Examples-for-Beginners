# File name: ...\\MyPythonXII\Unit2\PyChap02\chouse.py
class Housing:
    REG_NO = COST = 0
    HNAME = HTYPE = " "
    def __init__(self): # Constructor
        self.REG_NO = self.COST = 0        
    def Read_HouseData(self):
        while True:
            self.REG_NO = int(input("Enter house no. : "))
            if (self.REG_NO >= 10 and self.REG_NO <= 1000):
                break;
            else:
                print("House no. must be in between 10-1000")
        
        self.HNAME = input("Enter house owner's name : ")            
        houseType = ["HIG", "MIG", "LIG"]
        while True:
            self.HTYPE = input("Enter house type : ")
            self.HTYPE = self.HTYPE.upper()
            if (self.HTYPE in houseType):
                break
            else:
                print("House type must be HIG, MIG or LIG")
        self.COST = float(input("Enter house cost : "))        
    def Display_House(self):
        print("Registratin no. : ", self.REG_NO)
        print("House owner's name : ", self.HNAME)
        print("House type : ", self.HTYPE)
        print("House cost : ", self.COST)
        
H = Housing()
H.Read_HouseData()
H.Display_House()
