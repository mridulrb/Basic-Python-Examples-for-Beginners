a=[input("Enter Elements")]
m=0
n=0
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        if((a[i][j])%2==0):
            m=m+a[i][j]
        elif((a[i][j])%2==1):
            n=n+a[i][j]
print a[i][j]
print "Sum of even no.s",m
print "Sum of odd no.s",n

