a=list(input("Enter elements"))
b=list(input("Enter elements"))
c=list()
for i in range(0,len(a)):
    if(a[i]%2==0):
        c=c+[a[i]]
for j in range(0,len(b)):
    if(b[j]%2==0):
        c=c+[b[j]]
for j in range(len(b)-1,0,-1):
    if(b[j]%2==1):
        c=c+[b[j]]
for i in range(len(a)-1,0,-1):
    if(a[i]%2==1):
        c=c+[a[i]]
print c

        
