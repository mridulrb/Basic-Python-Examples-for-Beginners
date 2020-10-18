d1=[input("Enter elements")]
step=input("Enter columns")
a=[]
for i in range(0,len(d1),step):
    a=a+[d1[i:i+step]]
for j in range(0,len(a)):
    for k in range(0,len(a[j])):
        print a[j][k],
    print
