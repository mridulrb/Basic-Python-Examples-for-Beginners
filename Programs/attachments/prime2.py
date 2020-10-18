n =input("enter any no to check prime or composite")
for i in range(2,n+1):
    if (n%i==0 ):
        print "it is a composite no"
        break
    else :
        print "its a prime no"
