import pickle
import os
def binfile():
    x=0
    while x==0:
        data1={}    
        ifile1=open("stud12.dat","ab")
        rno=input("enter rno")
        k=raw_input("enter name ")
        data1[rno]=k
        pickle.dump(data1,ifile1)
        print"press 0 to continue"
        x=input("enter your choice")
        
    ifile1.close()
    ifile=open("stud12.dat","rb")

    try:
        
        while True:
            y=pickle.load(ifile)
            print y
    except EOFError:
        pass
    ifile.close()
    
def binsearchfile():
    ifile2=open("stud12.dat","rb")
    rno=input("Enter rnoto search")
    
    n=0
    try:
        
        while True:
            y=pickle.load(ifile2)
            for k in y:
                if k==rno:
                   print "hurray found it +++++++++",y
                   n=1
    except EOFError:
        pass
    ifile2.close()
    if n==0:
           print "sorry, record not found"
    
def modify():
    ifile1=open("temp.dat","wb")
    ifile2=open("stud12.dat","rb")
    rno=input("Enter rnoto modify")
    n=0
    a={}
    try:
        
        while True:
            y=pickle.load(ifile2)
            for k in y:
                if k==rno:
                    print "hurray found it +++++++++",y,"please enter new details"
                    r=input("enter rno")
                    j=raw_input("enter name ")
                    a[r]=j
                    y=a
                    pickle.dump(y,ifile1)
                    n=1
                else:
                    pickle.dump(y,ifile1)
    except EOFError:
        pass
    ifile2.close()
    ifile1.close()
    if n==0:
        print "sorry, record not found"
    os.remove("stud12.dat")
    os.rename("temp.dat","stud12.dat")

def insert():
    ifile1=open("temp.dat","wb")
    ifile2=open("stud12.dat","rb")
    rno=input("Enter record no. after which you want to insert")
    n=0
    c=0
    a={}
    try:
        
        while True:
            y=pickle.load(ifile2)
            for k in y:
                if k==rno:
                    print "hurray found it +++++++++",y
                    pickle.dump(y,ifile1)
                    print "please enter new details"
                    r=input("enter rno")
                    j=raw_input("enter name ")
                    a[r]=j
                    y=a
                    pickle.dump(y,ifile1)
                    n=1
                else:
                    pickle.dump(y,ifile1)
    except EOFError:
        pass
    ifile2.close()
    ifile1.close()
    if n==0:
        print "sorry, record not found"
    os.remove("stud12.dat")
    os.rename("temp.dat","stud12.dat")

def insert1():
    ifile1=open("temp.dat","wb")
    ifile2=open("stud12.dat","rb")
    no=input("Enter record no.where you want to insert")
    n=0
    c=0
    a={}
    try:
        
        while True:
            y=pickle.load(ifile2)
            for k in y:
                
                c=c+1
                if c==no:
                    print "please enter new details"
                    r=input("enter rno")
                    j=raw_input("enter name ")
                    a[r]=j
                    pickle.dump(a,ifile1)
                    pickle.dump(y,ifile1)
                    
                    n=1
                else:
                    pickle.dump(y,ifile1)
                
                    
    except EOFError:
        pass
    ifile2.close()
    ifile1.close()
    if n==0:
        print "sorry, record not found"
    os.remove("stud12.dat")
    os.rename("temp.dat","stud12.dat")




def fdel():
    ifile1=open("temp.dat","wb")
    ifile2=open("stud12.dat","rb")
    rno=input("Enter rnoto delete")
    n=0
    try:
        
        while True:
            y=pickle.load(ifile2)
            for k in y:
                if k==rno:
                    print "hurray found it +++++++++",y,"record deketed"
                    n=1
                else:
                    pickle.dump(y,ifile1)
    except EOFError:
        pass
    ifile2.close()
    ifile1.close()
    if n==0:
        print "sorry, record not found"
    os.remove("stud12.dat")
    os.rename("temp.dat","stud12.dat")

    
def disp():
    ifile=open("stud12.dat","rb")

    try:
        
        while True:
            y=pickle.load(ifile)
            print y
    except EOFError:
        pass
    ifile.close()

    
def namesearch():
    ifile2=open("stud12.dat","rb")
    rname=raw_input("Enter name to search")
    
    n=0
    try:
        
        while True:
            y=pickle.load(ifile2)
            for k,m in y.items():
                if m==rname:
                   print "hurray found it +++++++++",y
                   n=1
    except EOFError:
        pass
    ifile2.close()
    if n==0:
        print "sorry, record not found"

def main():
    
    #os.remove("stud12.dat") 
    binfile()
    binsearchfile()
    fdel()
    disp()
    modify()
    disp()
    insert()
    disp()
    insert1()
    disp()
    namesearch()
    
main()
