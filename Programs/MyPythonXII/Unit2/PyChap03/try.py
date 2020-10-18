class School:
    A = 0
    def INPUT(self):
        self.A = int(input("Enter A: "))
        self.B = int(input("Enter B: "))
        self.C = int(input("Enter C: "))
    def OUTPUT(self):
        print(self.A, ' ', self.B, ' ', self.C)
class Dept:
    __X = 0
    def IN(self):
        self.__X = int(input("Enter X: "))
        self.Y = int(input("Enter Y: "))        
    def OUT(self):
        print(self.A, ' ', self.B, ' ', self.C)
        print(self.X, ' ', self.Y)
class Teacher(Dept, School):
    P = 0
    def ENTER(self):
        self.P = int(input("Enter P: "))
    def DISPLAY(self):
        Teacher.ENTER(self)
        School.INPUT(self)
        School.OUTPUT(self)
        Dept.IN(self)
        Dept.OUT(self)
        
        print(self.P)        

T = Teacher()
#T.ENTER()
T.DISPLAY()
