print "Palindrome"
n=input("Enter number")
s=0
new=n
k=0
while(n>=1):
    r=n%10
    s=(s*10)+r
    n=n/10
    k+=1
if (s==new) and (k%2==1):
    print ("It is a palindrome")
else:
    print ("It is not a palindrome")

