n=input("Enter")
rev=0
new=n
while(n>=1):
    r=n%10
    rev=rev+(r**3)
    n=n/10
if (rev==new):
        print "It is a Armstrong no."
else:
        print "It is not "