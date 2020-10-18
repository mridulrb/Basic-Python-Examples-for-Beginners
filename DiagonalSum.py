n=list(input("Enter the nested list: "))
x,y=0,0
for i in range(0,len(n)):
    for j in range(0,len(n[i])):
        if (i==j):
            x+=n[i][j]
        if (i+j==(len(n)-1)):
            y+=n[i][j]
print ("The sum of left to right diagonal is",x)
print ("The sum of right to left diagonal is",y)


