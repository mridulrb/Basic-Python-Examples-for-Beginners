print ("Fibonacci Sequence")
x=0
y=1
n=input("Enter range")
print x
while (x<=n):
    y=x+y
    x=y-x
    if (x<=n):
        print (x)

