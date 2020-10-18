x=list(input("Enter list: "))
for i in range(0,len(x)):
    for j in range(0,len(x)-1):
        if x[j]>x[j+1]:
            x[j+1],x[j]=x[j],x[j+1]
print x
