print "Fibonacci Sequence"
n=input("Enter range")
x=0
y=1
print 0
while(x<=n):
    y=x+y
    x=y-x
    if(x<=n):
        print x
