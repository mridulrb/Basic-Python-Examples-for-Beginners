m=input("Enter no of records:")
k=[]
for i in range(m):
    data=input("Enter elements:")
    k+=[data]
n=input("Enter no of records:")
l=[]
for i in range(n):
    data=input("Enter elements:")
    l+=[data]
k+=l
print k
#Binary Sort
for i in range(len(k)):
    for j in range(len(k)-1):
        if(k[j]>k[j+1]):
            k[j],k[j+1]=k[j+1],k[j]
print k
