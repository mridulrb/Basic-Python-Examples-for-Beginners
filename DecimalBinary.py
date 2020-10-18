print ("Decimal to Binary Conversion")
n=input("Enter Decimal data type")
bn=0
k=0
while(n>0):
    r=n%2
    n=n/2
    bn=bn+(r*(10**k))
    k=k+1
print (bn)
