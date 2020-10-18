x=list()
n=input("Enter no. of elements")
for i in range(n):
    element=input("Enter elemnets")
    x+=[element]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if (x[i]>x[j]):
            x[i],x[j]=x[j],x[i]
print (x)

