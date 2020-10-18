a=[1,2,3,4,5,6]
l=len(a)
m=[]
n=[]
for j in range(1,l+1):
    for i in range(j):
        n=n+[a[i]]
    for k in range(j,l):
        n=n+[0]
    m=m+[n]
    n=[]
for c in range(l):
    for d in range(l):
        print m[c][d],
    print
