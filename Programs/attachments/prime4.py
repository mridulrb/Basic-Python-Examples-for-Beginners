n=input("Enter any value")
for i in range(2,n):
     if (n%i==0):
           print "it is a composite number"
           break
else:
           print "it is prime"
