import pickle
x=0
while x==0:
    data1={}    
    ifile1=open("stud.dat","ab")
    rno=input("enter rno")
    k=raw_input("enter name ")
    data1[rno]=k
    pickle.dump(data1,ifile1)
    print "do you want to continue , press 0 to do so"
    x=input("your choice")
ifile1.close()

ifile=open("stud.dat","rb")
try:
    while True:
        y=pickle.load(ifile)
        print y
except EOFError:
    pass

ifile.close()
    
