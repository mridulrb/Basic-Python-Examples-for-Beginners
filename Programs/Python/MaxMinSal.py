import pickle
import os
def binfile():
    x=0
    while x==0:
        d1={}
        d2={}
        y=open("emp.dat","wb")
        name=raw_input("Enter name:")
        salary=input("Enter salary:")
        desig=raw_input("Enter designation:")   
        d2['designation']=desig
        d2['salary']=salary
        d1[name]=d2
        pickle.dump(d1,y)
        print"press 0 to continue"
        x=input("enter your choice")
    y.close()
    y=open("emp.dat","rb")
    try:
        while True:
            l=pickle.load(y)
            print l
    except EOFError:
        pass
    y.close()
def maxmins():
    x=open("emp.dat","rb")
    maxs=0
    mind=pickle.load(x)
    a=mind.keys()
    b=a[0]
    mins=mind[b]['salary']
    maxd={}
    mind={}
    try:
        while True:
            m=pickle.load(x)
            l=m.keys()
            n=l[0]
            if(m[n]['salary']>maxs):
                maxd=m
                maxs=m[n]['salary']
            if(m[n]['salary']<mins):
                mins=m[n]['salary']
                mind=m
    except EOFError:
        pass
    print "Employee with highest salary",maxd
    print "Employee with lowest salary",mind
    x.close()
binfile()
maxmins()
