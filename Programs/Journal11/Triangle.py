list1=list(input("enter no"))
for i in range(0,len(list1)):
    for j in range(0,len(list1[i])):
        if(i==j or i<j):
            print list1[i][j],
    print
for i in range(0,len(list1)):
    for j in range(0,len(list1[i])):
        if(i==j or i>j):
            print list1[i][j],
    print
     
            
