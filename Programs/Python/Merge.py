x=[3,2,1,7,6,3]
y=[9,3,5,6,2,8,10]
m=len(x)
n=len(y)
l=m+n
z=[]
z=range(l)
p=0
for i in range(m):
    if(x[i]%2!=0):
        z[p]=x[i]
        p=p+1
for a in range(n):
    if(y[a]%2!=0):
        z[p]=y[a]
        p=p+1
k=len(z)-1
for b in range(m):
    if(x[b]%2==0):
        z[k]=x[b]
        k=k-1
for r in range(n):
    if(y[r]%2==0):
        z[k]=y[r]
        k=k-1
print x
print y
print z
