def primecheck(x,y):
    n=0
    for i in range(x+1,y):
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            print (i,"is a prime no")
            n+=i
    print ('The sum is',n)
x=input("Enter initial value ")
y=input("Enter final value ")
primecheck(x,y)

