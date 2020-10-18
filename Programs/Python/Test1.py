l=[]
n=input("Enter range:")
for i in range(n):
    a=()
    pno=raw_input("Enter no:")
    pname=raw_input("Enter name:")
    points=input("Enter points:")
    a=(pno,pname,points)
    l+=[a]
print l
b=len(l)
for j in range(b):
    for k in range(b-1):
        if(l[k][2]<l[k+1][2]):
            l[k],l[k+1]=l[k+1],l[k]
print l
