x=input("Enter number of elements")
n=list()
for i in range(1,x+1):
    y=input("Enter elements")
    n=n+[y]
print "Insert an element"
y=input("Enter element to be inserted")
x=input("Enter position")
n.insert(x,y)
print n
print "Delete an element"
m=input("Enter position of element to be deleted")
del n[m]
print n
