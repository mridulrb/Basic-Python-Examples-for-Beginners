n=input("Enter Rows:")
m=input("Enter Columns:")
a=()
b=()
sumld=0
sumrd=0
for i in range(n):
    for j in range(m):
        t=input("Enter element:")
        c=(t)
        b=b+(c,)
    a=a+((b),)
    b=()
for k in range(len(a)):
    for l in range(len(a[k])):
        print a[k][l],
    print
maxno=0
for k in range(len(a)):
    for l in range(len(a[k])):
        if(a[k][l]>maxno):
            maxno=a[k][l]
print "Largest Element:",maxno
for x in range(len(a)):
    for y in range(len(a[x])):
        if(x==y):
            sumld=sumld+a[x][y]
        if(x+y==(len(a)-1)):
            sumrd=sumrd+a[x][y]
print "Sum of Left Diagonal:",sumld
print "Sum of Right Diagonal:",sumrd
for u in range(len(a)):
    srow=0
    for v in range(len(a[u])):
        srow+=a[u][v]
    print "Sum of Row",u+1,"is:",srow
for p in range(m):
    scol=0
    for q in range(n):
        scol+=a[q][p]
    print "Sum of Column",p+1,"is:",scol
print "Upper Triangle"
for r in range(len(a)):
    for s in range(len(a[r])):
        if(r<=s):
            print a[r][s],
        else:
            print " ",
    print
print "Lower Triangle"
for r in range(len(a)):
    for s in range(len(a[r])):
        if(r>=s):
            print a[r][s],
        else:
            print " ",
    print        
