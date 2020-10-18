list1=list(input("enter no"))
sumeven=0
sumodd=0
for i in range(0,len(list1)):
    for j in range(0,len(list1[i])):
        print list1[i][j],
    print
for i in range(0,len(list1)):
    for j in range(0,len(list1[i])):
        if ((list1[i][j])%2==0):
            sumeven=sumeven+(list1[i][j])
        if ((list1[i][j])%2!=0):
            sumodd=sumodd+(list1[i][j])
print sumeven
print sumodd
