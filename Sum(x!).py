s=0
a=1
x=input("Enter number")
n=input("Enter number of terms")
for i in range(1,n+1):
    k=1
    for j in range(1,i+a):
        k=k*j
    if (i%2==0):
        s=s-(float(x**i)/k)
    else:
        s=s+(float(x**i)/k)
    a+=1
print ("The sum is",s)

