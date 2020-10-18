import os
import pickle
class school:
    def __init__(self):
        self.grno=0
        self.name="abc"
    def putdata(self):
        self.grno=input("Enter Student GR No.:")
        self.name=raw_input("Enter Student name:")
    def display(self):
        print self.grno,self.name
def create():
    x=open("student.dat","wb")
    n=input("Enter no of records:")
    s=school()
    for i in range(n):
        s.putdata()
        pickle.dump(s,x)
    x.close()
def append():
    x=open("student.dat","ab")
    s=school()
    s.putdata()
    pickle.dump(s,x)
    x.close()
def search():
    x=open("student.dat","rb")
    grno=input("Enter Student GR No.:")
    s=school()
    y=0
    try:
        while True:
            s=pickle.load(x)
            if(s.grno==grno):
                s.display()
                y+=1
    except EOFError:
        pass
    if(y==0):
        print "Record not found!"
    x.close()
def display():
    x=open("student.dat","rb")
    s=school()
    try:
        while True:
            s=pickle.load(x)
            s.display()
    except EOFError:
        pass
    x.close()
def modify():
    x=open("student.dat","rb")
    y=open("newfile.dat","wb")
    grno=input("Enter Student GR No.:")
    s=school()
    try:
        while True:
            s=pickle.load(x)
            if(s.grno==grno):
                a=school()
                a.putdata()
                pickle.dump(a,y)
            else:
                pickle.dump(s,y)
    except EOFError:
        pass
    x.close()
    y.close()
    os.remove("student.dat")
    os.rename("newfile.dat","student.dat")
def insert():
    x=open("student.dat","ab")
    n=input("Enter no of records:")
    for i in range(n):
        s=school()
        s.putdata()
        pickle.dump(s,x)
    x.close()
while True:
    print "    1)Create"
    print "    2)Append"
    print "    3)Display"
    print "    4)Search"
    print "    5)Modify"
    print "    6)Insert"
    print "    7)Exit"
    choice=input("Enter choice:")
    if(choice==1):
        create()
    elif(choice==2):
        append()
    elif(choice==3):
        display()
    elif(choice==4):
        search()
    elif(choice==5):
        modify()
    elif(choice==6):
        insert()
    elif(choice==7):
        break
    else:
        "Print Invalid Choice!"
