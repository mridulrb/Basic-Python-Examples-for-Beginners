class SpecialEngine(object):
    def __init__(self,p):
        self.power=p
    def ignition(self):
        print "Engine started"
class Car(object):
    def __init__(self,clr,seats):
        self.colour=clr
        self.seatingCapacity=seats
    def changeGears(self,gr):
        print "changed to gear",gr
    def turn(self,direction):
        print "turned to ",direction," direction"
class RacingCar(SpecialEngine,Car):
    def __init__(self,clr,seats,p,tr,spd):
        SpecialEngine.__init__(self,p)
        Car.__init__(self,clr,seats)
        self.turnRadius=tr
        self.speed=spd
        print "Racing Car instance created"
    def start(self):
        self.ignition()
        self.changeGears(2)
        print "Racing Car starts-ready to vroom"
rcar=RacingCar('Blue',2,750,6,200)
rcar.start()
rcar.turn("left")
            
