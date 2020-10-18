def fact(n):
    for i in range(1,n):
        n=n*i
    return n
print "Choose from the following"
print "A)Permutation"
print "B)Combination"
print "C)Sigma(x^n/2n!)"
choice=raw_input("Enter choice(Capital Letters)")
if(choice=="A"):
    a=input("Enter value for n")
    b=input("Enter value for r")
    permutation= (fact(a))/(fact(a-b))
    print permutation
if(choice=="B"):
    a=input("Enter value for n")
    b=input("Enter value for r")
    combination=(fact(a))/(fact(b))*(fact(a-b))
    print combination
if(choice=="C"):
    a=input("Enter value for x")
    b=input("Enter value for n")
    c=0
    for j in range(1,a+1):
        d=((j**b)/float(2*fact(b)))
        c=c+d
    print c
