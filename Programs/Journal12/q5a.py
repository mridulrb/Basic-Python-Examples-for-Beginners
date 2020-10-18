n=input("Enter no of elements:")
l=[]
for i in range(n):
    data=input("Enter data:")
    l+=[data]
while True:
    print "    1)Linear Search"
    print "    2)Binary Search"
    print "    3)Exit"
    choice=input("Enter choice:")
    if(choice==1):
        x=input("Enter element to be searched:")
        y=0
        for i in range(n):
            if(l[i]==x):
                y+=1
                print "Data found at",i+1,"position"
        if(y==0):
            print "Data not found!"
    elif(choice==2):
        #Selection Sort
        for i in range(n):
            for j in range(i+1,n):
                if(l[i]>l[j]):
                    l[i],l[j]=l[j],l[i]
        print "Sorted list is:",l
        x=input("Enter element to be searched:")
        f=0
        s=len(l)-1
        a=[]
        while(f<=s or s>=0):
            m=(f+s)/2
            if(l[m]==x):
                print "Element found at",m+1,"position"
                break
            elif(x>l[m]):
                f=m+1
            elif(x<l[m]):
                s=m-1
        if(f>s):
            print "Data not found"
    elif(choice==3):
        break
    
