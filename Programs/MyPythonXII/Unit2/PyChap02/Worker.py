# File name: ...\\MyPythonXII\Unit2\PyChap02\Worker.py
class Worker:
    Wno = 0
    Wname = " "
    Hrwrk = 0
    Wgrate = 0
    def __init__(self, hr = 40): # Default parameter hr = 40
        if hr < 40 :
            self.Hrwrk = 40
        else:
            self.Hrwrk = hr        
    def Worker_Indata(self):
        print ("Enter worker's data...")
        self.Wno = int(input("Enter worker no.: "))
        self.Wname = input("Enter name: ")
        self.Hrwrk = float(input("Enter total hours worked: "))
        if self.Hrwrk < 40:
            self.Hrwrk = 40
        self.Wgrate = float(input("Enter hourly wage rate: "))
        self.Worker_Outdata()
    def Calc_Wage(self):
        Wage = (40 * self.Wgrate) + ((self.Hrwrk - 40) * (self.Wgrate + self.Wgrate * 0.15))
        print("Total wage is: %.2f" % Wage)
    def Worker_Outdata(self):
        print ("Worker's informatio...")
        print("Worker no.: ", self.Wno)
        print("Name: ", self.Wname)
        print("Hours worked: ", self.Hrwrk)
        print("Hourly wage rate.: ", self.Wgrate)
        self.Calc_Wage()
        
        
Wk = Worker()
Wk.Worker_Indata()

        			
