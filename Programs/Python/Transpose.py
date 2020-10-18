m=input("Enter rows:")
n=input("Enter column:")
a=[]
for i in range(m):
    b=[]
    for j in range(n):
        x=input("Enter element:")
        b+=[x]
    a+=[b]
for i in range(m):
    for j in range(n):
        print a[i][j],
    print
c=[]
for i in range(n):
    d=[]
    for j in range(m):
         d+=[a[j][i]]
    c+=[d]
print "Transpose"
for i in range(n):
    for j in range(m):
        print c[i][j],
    print

