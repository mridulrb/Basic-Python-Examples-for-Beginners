n=list(input("Enter list"))
n.sort()
x=input("Enter item to be searched")
b=0
e=len(n)-1
while(b<=e):
    m=(b+e)/2
    if (n[m]==x):
        print "Found",x,"in location",m+1
        break
    elif(x>n[m]):
        b=m+1
    else:
        e=m-1
if(b>e):
    print ("Not found")
