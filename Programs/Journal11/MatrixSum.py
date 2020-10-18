list1=list(input("enter no"))
total=0
n=0
for i in range(0,len(list1)):
    for j in range(0,len(list1[i])):
        n=n+1
        total=total+(list1[i][j])
print total
avg=total/float(n)
print avg

