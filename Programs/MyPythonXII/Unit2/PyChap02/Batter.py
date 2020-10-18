# File name: ...\\MyPythonXII\Unit2\PyChap02\Batter.py
class Batter:
    Bcode = Innings = Notouts = Runs = Batavg = 0
    Bname = " "    
    def ReadData(self):
        print ("Enter batters's data...")
        self.Bcode = int(input("Enter code: "))
        self.Bname = input("Enter name: ")
        self.Innings = float(input("Enter total innings: "))
        self.Notouts = float(input("Enter total notouts: "))
        self.Runs = float(input("Enter total runs: "))
        self.DisplayData()
    def __CalcAvg(self):
        self.Batavg = self.Runs / (self.Innings - self.Notouts)
        print("Batter average is: %.2f" % self.Batavg)
    def DisplayData(self):
        print ("Batter's informatio...")
        print("Code: ", self.Bcode)
        print("Name: ", self.Bname)
        print("Innings: ", self.Innings)
        print("Notouts: ", self.Notouts)
        print("Runs: ", self.Runs)
        self.__CalcAvg()
        
        
B = Batter()
B.ReadData()

        			
