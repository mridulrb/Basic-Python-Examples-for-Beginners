x=input("Enter number")
y=input("Enter number")
a=min(x,y)
b=max(x,y)
c=list()    
if(b%a==0):
    print "LCM is",b
    print "HCF is",a
elif(a!=b):
    for i in range(1,a+1):
        if(x%i==0 and y%i==0):
            c=c+[i]
        d=c[0]
        for j in range(1,len(c)):
            if(d<c[j]):
                d=c[j]
        print d
else:
    print "LCM is",x*y
        
