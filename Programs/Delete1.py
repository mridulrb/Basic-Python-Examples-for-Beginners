n=list(input("Enter elements"))
a=input("Enter element")
for k in range(0,len(n)):
    if(n[k]==a):
        x=k
    else:
        continue
for i in range(x+1,len(n)):
    n[i-1]=n[i]
for j in range(0,len(n)-1):
    print n[j],

