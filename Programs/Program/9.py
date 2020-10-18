x=input("Enter number")
y=input("Enter number")
if(x!=y):
    for i in range(1,y+1):
        print x,"*",i,"=",x*i
    for j in range(1,x):
        print y,"*",j,"=",y*j
elif(x==y):
    for i in range(1,y+1):
        print x,"*",i,"=",x*i
    for j in range(1,x+1):
        print y,"*",j,"=",y*j
