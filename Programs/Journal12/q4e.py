class Vehicle(object):
    def __init__(self,l=0,w=0):
        self.length=l
        self.width=w
    def define(self):
        print "Vehicle with length",self.length,"in & width",self.width,"in"
class Car(Vehicle):
    def __init__(self,clr,seats,l,w):
        Vehicle.__init__(self,l,w)
        self.colour=clr
        self.seatingCapacity=seats
    def changeGears(self,gr):
        print "changed to gear",gr
    def turn(self,direction):
        print "turned to",direction,"direction"
class RacingCar(Car):
    def __init__(self,clr,seats,l,w,tr,spd):
        Car.__init__(self,clr,seats,l,w)
        self.turnRadius=tr
        self.speed=spd
        print "Racing Car instance created"
    def start(self):
        self.define()
        self.changeGears(2)
        print "Racing car starts - ready to vroom!"

rcar=RacingCar("Blue",2,206,78.5,6,200)
rcar.start()
rcar.turn("left")
