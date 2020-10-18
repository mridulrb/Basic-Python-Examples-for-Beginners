n=list(input("Enter elements"))
x=input("Enter position of element to be deleted")
for i in range(x,len(n)):
    n[i-1]=n[i]
for j in range(0,len(n)-1):
    print n[j],
