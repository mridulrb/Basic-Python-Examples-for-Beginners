class school:
    def __init__(self):
        self.grno=input("Enter Student GR No.:")
        self.name=raw_input("Enter Student name:")
    def display(self):
        print self.grno,self.name
n=input("Enter no of records:")
for i in range(n):
    s=school()
for j in range(n):
    s.display()
