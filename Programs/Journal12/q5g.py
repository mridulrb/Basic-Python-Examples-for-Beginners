m=input("Enter rows:")
n=input("Enter columns:")
a=[]
for i in range(m):
    b=[]
    for j in range(n):
        x=input("Enter element:")
        b+=[x]
    a+=[b]
def display():
    for i in range(m):
        for j in range(n):
            print a[i][j],
        print
def transpose():
    c=[]
    for i in range(n):
        d=[]
        for j in range(m):
            d+=[a[j][i]]
        c+=[d]
    for i in range(n):
        for j in range(m):
            print c[i][j],
        print
def sumdiagonal():
    sumld=0
    sumrd=0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(i==j):
                sumld=sumld+a[i][j]
            if(i+j==(len(a)-1)):
                sumrd=sumrd+a[i][j]
    print "Sum of Left Diagonal:",sumld
    print "Sum of Right Diagonal:",sumrd
def matrixtriangle():
    print "Upper Triangle"
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(i<=j):
                print a[i][j],
            else:
                print " ",
        print
    print "Lower Triangle"
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(i>=j):
                print a[i][j],
            else:
                print " ",
        print
def largestelement():
    x=a[0][0]
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            if(a[i][j]>x):
                x=a[i][j]
    print "The greatest number is",x
def sumrowcol():
    for i in range(len(a)):
        srow=0
        for j in range(len(a[i])):
            srow+=a[i][j]
        print "Sum of Row",i+1,"is:",srow
    for i in range(m):
        scol=0
        for j in range(n):
            scol+=a[j][i]
        print "Sum of Column",i+1,"is:",scol
def matrixsum():
    p=input("Enter rows:")
    q=input("Enter columns:")
    if(p==m and q==n):
        x=[]
        for i in range(m):
            y=[]
            for j in range(n):
                d=input("Enter element:")
                y+=[d+a[i][j]]
            x+=[y]
        for i in range(m):
            for j in range(n):
                print x[i][j],
            print
    else:
        print "Matrix Addition is not possible as Row of Second Matrix is not equal to Column of First Matrix!"
def matrixmul():
    p=input("Enter rows:")
    q=input("Enter columns:")
    if(p==n):
        x=[]
        for i in range(n):
            y=[]
            for j in range(q):
                d=input("Enter data:")
                y+=[d]
            x+=[y]
        c=[]
        for i in range(m):
            e=[]
            for j in range(q):
                d=0
                for k in range(n):
                    d=d+a[i][k]*x[k][j]
                e+=[d]
            c+=[e]     
        for i in range(len(c)):
            for j in range(len(c[i])):
                print c[i][j],
            print
    else:
        print "Matrix Multiplication is not possible as Order of the two Matrices is not same!"
while True:
    print "    1)Display"
    print "    2)Transpose"
    print "    3)Sum of diagonals"
    print "    4)Upper & Lower Triangle"
    print "    5)Largest Element"
    print "    6)Sum of Rows & Column"
    print "    7)Sum of Matrices"
    print "    8)Product of Matrices"
    print "    9)Exit"
    choice=input("Enter choice:")
    if (choice==1):
        display()
    elif (choice==2):
        transpose()
    elif (choice==3):
        sumdiagonal()
    elif (choice==4):
        matrixtriangle()
    elif (choice==5):
        largestelement()
    elif (choice==6):
        sumrowcol()
    elif (choice==7):
        matrixsum()
    elif (choice==8):
        matrixmul()
    elif (choice==9):
        break
    else:
        print "Invalid choice!"

    
    
    
