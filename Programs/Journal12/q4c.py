class Car(object):
    def __init__(self,clr,seats):
        self.colour=clr
        self.seatingcapacity=seats
        print "Car instance created"
    def accelerate(self,time,direction):
        print "Inside accelerate method"
    def turn(self,direction):
        print "Inside Turn Method"
    def __str__(self):
        string=self.colour+" coloured Car with "+str(self.seatingcapacity)+" seats."
        return string
class RacingCar(Car):
    def __init__(self,clr,seats,tr,spd):
        Car.__init__(self,clr,seats)
        self.turnRadius=tr
        self.avgSpeed=spd
        print "RacingCar instance created"
    def __str__(self):
        string=self.colour+ " RacingCar with "+str(self.turnRadius)+" turn radius and speed "+str(self.avgSpeed)+"rpm"
        return string
mycar=Car("Blue",5)
rcar=RacingCar("Red",2,6,190)
print mycar
print rcar  
