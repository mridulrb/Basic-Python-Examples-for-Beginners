n=input("enter no")
m=n
k=0
while(n>=1):
    r=n%10
    k=(k*10)+r
    n=n/10
if (k==m):
    print"pallindrome"
else:
    print "no"
