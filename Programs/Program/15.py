n=[2,5,6,7,3,4]
print n
n.sort()
print n
m=input("Enter number of elements to be inserted")
for i in range(1,m+1):
    x=input("Enter position")
    y=input("Enter element")
    n.insert(x,y)
print n

    
