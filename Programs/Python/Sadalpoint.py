m=input("Enter rows:")
n=input("Enter columns:")
l=[]
for i in range(m):
    y=[]
    for j in range(n):
        x=input("Enter element:")
        y+=[x]
    l+=[y]
minl=[]
maxl=[]
for i in range(m):
    mine=l[i][0]
    for j in range(n):
        if(l[i][j]<mine):
            mine=l[i][j]
    minl+=[mine]
for i in range(n):
    maxe=0
    for j in range(m):
        if(maxe<l[j][i]):
            maxe=l[j][i]
    maxl+=[maxe]
f=0
for a in minl:
    for b in maxl:
        if(a==b):
            print a,"is Saddle point"
            f+=1
if(f==0):
    print "No Saddle point"
