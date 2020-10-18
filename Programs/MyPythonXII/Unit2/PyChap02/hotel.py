# File name: ...\\MyPythonXII\Unit2\PyChap02\hotel.py
class Hotel:
    def CheckIn(self):
        print ("Enter customer data...")
        self.RoomNo = int(input("Enter room no.: "))
        self.Name = input("Enter customer name: ")
        self.NoOfDays = int(input("Enter nummber of days stay: "))
        self.PerDayCharge = int(input("Enter per day charge: "))        
    def __ComputeCharge(self):
        self.Total = self.NoOfDays * self.PerDayCharge
        return self.Total
    def CheckOut(self):
        print ("Customer informatio...")
        print("Room no: ", self.RoomNo)
        print("Name: ", self.Name)
        print("Days stay: ", self.NoOfDays)
        print("Per day charge: ", self.PerDayCharge)
        print("Total charge", self.__ComputeCharge())
H = Hotel()
H.CheckIn()
H.CheckOut()

        			
