print ("Largest & Smallest Element")
x=list(input("Enter list: "))
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if (x[i]>x[j]):
            x[i],x[j]=x[j],x[i]
print ("The smallest number is",x[0])
print ("The largest number is",x[len(x)-1])

