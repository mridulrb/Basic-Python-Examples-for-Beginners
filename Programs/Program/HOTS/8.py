line="Raju C Jain"
line=line+" "
a=list()
for i in range(0,len(line)):
    if ((line[i]!=" ") ):
        a=a+[line[i]]
    else:
        for j in range(len(a)-1,-1,-1):
            print a[j],
        print " ",
        del a[:]
