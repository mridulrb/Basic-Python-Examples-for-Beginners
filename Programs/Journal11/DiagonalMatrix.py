list1=list(input("enter no"))
y=" "
length=len(list1)
print "Diagonal 1"
for i in range(0,len(list1)):
    for j in range(0,len(list1[i])):
        if(i==j):
            print y*j,list1[i][j]
print "Diagonal 2"
for i in range(0,len(list1)):
    for j in range(0,len(list1[i])):
        if((length-(i+j))==1):
            print y*j,list1[i][j] 

