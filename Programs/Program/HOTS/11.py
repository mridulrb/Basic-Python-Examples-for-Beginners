a=[1,2,3,4]
for i in range(1,len(a)+1):
    b=[[a]]*i
for j in range(0,len(b)):
    for k in range(0,len(b[j])):
        print b[j][k],
    print
