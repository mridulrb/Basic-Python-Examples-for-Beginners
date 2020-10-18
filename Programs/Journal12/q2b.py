t=()
n=input("Enter no of records:")
for i in range(n):
    data=input("Enter data:")
    t+=(data,)
even=()
odd=()
for i in t:
    if(i%2==0):
        even=even+(i,)
    else:
        odd=odd+(i,)
print even
print odd
