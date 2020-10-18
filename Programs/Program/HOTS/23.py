a=list(input("Enter elements"))
b=list(input("Enter elements"))
c=list()
if(len(a)==len(b)):
    for i in range(0,len(a)):
        c=c+[a[i]]+[b[len(b)-1-i]]
    print c
else:
    print "Enter lists with equal number of elements"
        
