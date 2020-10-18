x=list(input("Enter the nested list: "))
a=x[0][0]
for i in range(0,len(x)):
    for j in range(0,len(x[i])):
        if (x[i][j]>a):
            a=x[i][j]
print ("The greatest number is",a)

