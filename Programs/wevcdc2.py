def fact(n):
    a=1
    while True:
        a=a*n
        n=n-1
    return fact 
print "Choose from the following"
print "A)Permutation"
print "B)Combination"
print "C)Sigma(x^n/2n!)"
b=0
choice=raw_input("Enter choice(Capital Letters)")
if(choice=="A"):
    n=input("Enter value for n")
    r=input("Enter value for r")
    permutation= fact(n)/fact(n-r)
    print permutation
if(choice=="B"):
    n=input("Enter value for n")
    r=input("Enter value for r")
    combination=fact(n)/(fact(r)*fact(n-r))
    print combination
if(choice=="C"):
    x=input("Enter value for x")
    n=input("Enter value for n")
    z=0
    for i in range(1,x+1):
        a=(i**n/(2*fact(n))
        z=z+a
    print z
