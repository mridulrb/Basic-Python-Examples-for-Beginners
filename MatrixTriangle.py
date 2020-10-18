n=list(input("Enter nested list: "))
for i in range(0,len(n)):
    for j in range(0,len(n[i])):
        if(i<=j):
            print (n[i][j]),
        else:
            print " ",
    print
for i in range(0,len(n)):
    for j in range(0,len(n[i])):
        if(i>=j):
            print (n[i][j]),
        else:
            print " ",
    print

