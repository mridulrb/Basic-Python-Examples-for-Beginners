#Number Reverse
num=input("Enter number:")
l=len(str(num))
a=0
r=num
for i in range(l-1,-1,-1):
    b=r%10
    a+=(b*(10**i))
    if(r>10):
        r=r/10
    else:
        continue
print a
    
    
