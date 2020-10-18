class student:
    def __init__(self,a,b,c):
        self.name=a
        self.grno=b
        self.marks=c
    def accept(self):
        self.name=raw_input("Enter name:")
        self.grno=input("Enter GR no.:")
        self.marks=input("Enter marks:")
    def output(self):
        print self.grno,self.name,self.marks
n=input("Enter no. of records")
stud=[]
for i in range(n):
    stud1=student("Ravi",10,98)
    stud1.accept()
    stud+=[stud1]
maxs=0
j=0
mins=stud[0].marks
k=0
for i in range(n):
    if(stud[i].marks>maxs):
        maxs=stud[0].marks
        j=i
    elif(stud[i].marks<mins):
        mins=stud[i].marks
        k=i
print " Student with Highest Score",stud[j].output()
print " Student with Lowest Score",stud[k].output()

