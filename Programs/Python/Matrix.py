n=input("Enter order of Matrix:")
a=[]
b=[]
for i in range(n):
    for j in range(n):
        m=input("Enter element:")
        b=b+[m]
    a=a+[b]
    b=[]
for k in range(len(a)):
    for l in range(len(a[k])):
        print a[k][l],
    print 
