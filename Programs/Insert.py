m=list(input("enter list"))
a=input("Enter element to be inserted")
b=input("Enter position of element to be inserted")
n=m+[a]
for i in range(b,len(n)):
    n[i]=m[i-1]
n[b-1]=a
print n,
