print "Bubble Sort"
x=list(input("Enter list"))
n=len(x)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(x[j]>x[j+1]):
            x[j],x[j+1]=x[j+1],x[j]
print (x)
       
