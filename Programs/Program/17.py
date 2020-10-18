n=list(input("Enter the nested list: "))
x,y=0,0
for i in range(0,len(n)):
    for j in range(0,len(n[i])):
        print n[i][j],
    print
for m in range(0,len(n)):
    for p in range(0,len(n[i])):
        if (m==p):
            x+=n[m][p]
        if (m+p==(len(n)-1)):
            y+=n[m][p] 
for i in range(0,len(n)):
    print "Sum of row",i+1,"is",sum(n[i])
for j in range (0,len(n)):
    s=0
    for k in range(0,len(n[i])):
        s+=n[k][j]
    print "Sum of column",j+1,"is",s
print "The sum of left to right diagonal is",x
print "The sum of right to left diagonal is",y
