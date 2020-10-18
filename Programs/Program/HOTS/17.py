n=list(input("Enter marks"))
n.sort()
p=list(input("Enter percentage"))
p.sort()
first=n[0]
firstp=0
for i in range(0,len(n)):
    if(first<n[i]):
        first=n[i]
        firstp=p[i]
    else:
        continue
print "First",first,firstp
for i in range(0,len(n)):
    if(n[0]<n[i] and n[i]<first):
        second=n[i]
        secondp=p[i]
    else:
        continue
print "Second",second,secondp
