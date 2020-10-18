n=input("Enter no of elements:")
l=[]
for i in range(n):
    data=input("Enter data:")
    l+=[data]
for i in range(n):
    for j in range(i+1,n):
        l[i],l[j]=l[j],l[i]
print "List after swapping elements",l
