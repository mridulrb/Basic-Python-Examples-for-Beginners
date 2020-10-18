n=input("Enter no of elements:")
l=[]
for i in range(n):
    data=input("Enter data:")
    l+=[data]
while True:
    print "    1)Binary Sort"
    print "    2)Selection Sort"
    print "    3)Insertion Sort"
    print "    4)Exit"
    choice=input("Enter choice:")
    if(choice==1):
        for i in range(len(l)):
            for j in range(len(l)-1):
                if(l[j]>l[j+1]):
                    l[j],l[j+1]=l[j+1],l[j]
        print l
    elif(choice==2):
        for i in range(len(l)):
            p=i
            for j in range(i+1,n):
                if(l[p]>l[j]):
                    p=j
            l[p],l[i]=l[i],l[p]
        print l
    elif(choice==3):
        for i in range(1,len(l)):
            p=i-1
            m=l[i]
            while (p>=0 and l[p]>m):
                l[p+1]=l[p]
                p=p-1
            l[p+1]=m
        print l
    elif(choice==4):
        break
    else:
        print "Invalid Choice!"
