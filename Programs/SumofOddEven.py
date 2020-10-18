odd=1
even=2
x=0
y=0
n=input("Enter range")
while(odd<=n):
    x=odd+x
    odd=odd+2
print x
while(even<=n):
    y=even+y
    even=even+2
print y