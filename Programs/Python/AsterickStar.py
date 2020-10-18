x="*"
y=" "
n=3
for i in range(1,n+1):
    for r in range (1,9):
        print y,
    for k in range(i,n+1):
        print y,
    for j in range(1,i+1):
        print x,y,
    print '\n'
n=11
for i in range(n+1,4,-2):
    for k in range(i,n+1):
        print y,
    for j in range(1,i+1):
        print x,y,
    print '\n'

for i in range(7,n-2):
    for k in range(i,n+1):
        print y,
    for j in range(1,i+1):
        print x,y,
    print '\n'

l=3
for i in range(9,n+1):
    for k in range(n+1,i,-1):
        print y,
    for g in range(n+1,i,-1):
        print x,y,
    for s in range(0,l):
        print y,y,
    for q in range(n+1,i,-1):
        print x,y,
    l=l+3
    print '\n'
