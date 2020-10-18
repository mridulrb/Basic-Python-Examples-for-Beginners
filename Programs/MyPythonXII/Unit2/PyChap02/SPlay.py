# File name: ...\\MyPythonXII\Unit2\PyChap02\Splay.py
class Play:
    Playcode = Duration = Noofepisodes = 0
    Playtitle = " "
    def __init__(self): # Constructor
        self.Duration = 45
        self.Noofepisodes = 5        
    def NewPlay(self):
        self.Playcode = int(input("Enter play code : "))
        self.Playtitle = input("Enter play title : ")        
    def Moreinfo(self, a, b):
        self.Duration = a
        self.Noofepisodes = b
    def Showdata(self):
        print("Play code : ", self.Playcode)
        print("Play title : ", self.Playtitle)
        print("Duration : ", self.Duration)
        print("Number of episodes : ", self.Noofepisodes)
        
        
P = Play()
P.NewPlay()
a = float(input("Enter duration of play : "))
b = int(input("Enter no. of episodes : "))
P.Moreinfo(a, b)
P.Showdata()
        			
