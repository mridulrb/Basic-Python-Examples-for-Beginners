list1=list(input("enter no"))
a=0
b=0
c=0
d=0
for i in range(0,len(list1)):
    for j in range(0,len(list1[i])):
        a=a+list1[i][j]
        b=b+list1[j][i]
    print a
    print b
        
