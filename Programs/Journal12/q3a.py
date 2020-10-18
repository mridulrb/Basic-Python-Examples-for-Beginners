import pickle
import os
def createfile():
    x=0
    while x==0:
        d={}    
        y=open("emp.dat","wb")
        name=raw_input("Enter name:")
        salary=input("Enter salary:")
        d['Name']=name
        d['Salary']=salary
        pickle.dump(d,y)
        print"Press 0 to continue"
        x=input("Enter your choice:")
    y.close()
    y=open("emp.dat","rb")
    try:
        while True:
            l=pickle.load(y)
            print l
    except EOFError:
        pass
    y.close()
def modify():
    x=open("emp.dat","rb")
    y=open("newfile.dat","wb")
    name=raw_input("Enter Name of Employee:")
    f=0
    try:
        while True:
            l=pickle.load(x)
            if(l['Name']==name):
                emp={}
                emp['Name']=raw_input("Enter Name:")
                emp['Salary']=input("Enter Salary:")
                pickle.dump(emp,y)
                f=f+1
            else:
                pickle.dump(l,y)
    except EOFError:
        pass
    if(f==0):
        "Record Not Found"
    x.close()
    y.close()
    os.remove("emp.dat")
    os.rename("newfile.dat","emp.dat")
def addrecord():
    print "Adding a record"
    d={}    
    y=open("emp.dat","ab")
    name=raw_input("Enter Name:")
    salary=input("Enter Salary:")
    d['Name']=name
    d['Salary']=salary
    pickle.dump(d,y)
    y.close()
def deleterecord():
    x=open("emp.dat","rb")
    y=open("newfile.dat","wb")
    name=raw_input("Enter Name of Employee to be deleted:")
    f=0
    try:
        while True:
            l=pickle.load(x)
            if(l['Name']==name):
                continue
            else:
                pickle.dump(l,y)
    except EOFError:
        pass
    if(f==0):
        "Record Not Found"
    x.close()
    y.close()
    os.remove("emp.dat")
    os.rename("newfile.dat","emp.dat")
def searchrecord():
    x=open("emp.dat","rb")
    name=raw_input("Enter Name of Employee to be searched:")
    try:
        while True:
            l=pickle.load(x)
            if(l['Name']==name):
               print l
    except EOFError:
        pass
def display():
    x=open("emp.dat","rb")
    try:
        while True:
            y=pickle.load(x)
            print y
    except EOFError:
        pass
    x.close()
while True:
    print "     1)Create a file"
    print "     2)Modify a record"
    print "     3)Add a record"
    print "     4)Delete a record"
    print "     5)Search a record"
    print "     6)Display"
    print "     7)Exit"
    choice=input("Enter choice:")
    if(choice==1):
        createfile()
    elif(choice==2):
        modify()
    elif(choice==3):
        addrecord()
    elif(choice==4):
        deleterecord()
    elif(choice==5):
        searchrecord()
    elif(choice==6):
        display()
    elif(choice==7):
        break
    else:
        "Invalid Choice"
