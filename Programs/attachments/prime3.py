n=input("enter range")
for j in range(2,n +1):
    for i in range(2,j):
        if (j%i==0):
            break
        else:
            print j
            break
