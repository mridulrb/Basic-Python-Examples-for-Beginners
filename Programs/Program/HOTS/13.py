n=list(input("Enter the nested list: "))
for i in range(0,len(n)):
    for j in range(0,len(n[i])):
        print n[i][j],
    print
s=0
a=0
for i in range(0,len(n)):
    for j in range(0,len(n[i])):
        if(i<=j):
            a=a+1
            s=s+n[i][j]
print s
print s/float(a)
p=1
for i in range(0,len(n)):
    for j in range(0,len(n[i])):
        if(i>=j):
            p=p*n[i][j]
print p
pr=1
for i in range(0,len(n)):
    for j in range(0,len(n[i])):
        if(i+j>=2):
            pr=pr*n[i][j]
    
print pr
su=0
b=0
for i in range(0,len(n)):
    for j in range(0,len(n[i])):
        if(i+j<=2):
            b=b+1
            su=su+n[i][j]
print su
print su/float(b)
        
