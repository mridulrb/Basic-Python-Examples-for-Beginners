n=input("Enter no of elements:")
l=[]
for i in range(n):
    data=input("Enter data:")
    l+=[data]
#Check if list is sorted or unsorted
asc=0
dsc=0
for i in range(len(l)-1):
    if(l[i]<l[i+1]):
        asc+=1
    if(l[i]>l[i+1]):
        dsc+=1
if(asc==(len(l)-1)):
    print "Ascending"
    a=asc
elif(dsc==(len(l)-1)):
    print "Descending"
    a=dsc
elif(asc!=(len(l)-1) or dsc!=(len(l)-1)):
    print "Not Sorted"
    a=n
while True:
    print "    1)Insert"
    print "    2)Delete"
    print "    3)Exit"
    choice=input("Enter choice:")
    if(choice==1):
        if(a==asc):
            l.append(None)
            d=input("Enter data to be inserted:")
            f=0
            for i in range(len(l)):
                if(d<l[i]):
                    p=i
                    f=1
                    break
            if (f==0):
                p=n-i
                l[p]=d
            else:
                g=len(l)
                while(g>p):
                    l[g-1]=l[g-2]
                    g=g-1
            l[p]=d
            print l
        if(a==dsc):
            l.append(None)
            d=input("Enter data to be inserted:")
            f=0
            for i in range(len(l)):
                if(d>l[i]):
                    p=i
                    f=1
                    break
            if (f==0):
                p=n-i
                l[p]=d
            else:
                g=len(l)
                while(g>p):
                    l[g-1]=l[g-2]
                    g=g-1
            l[p]=d
            print l
        else:
            d=input("Enter data to be inserted:")
            l+=[d]
            print l
    elif(choice==2):
        d=input("Enter data to be deleted:")
        for i in range(len(l)):
          if(d==l[i]):
              p=i
              break
        while(p<=(len(l)-2)):
            l[p]=l[p+1]
            p=p+1
        l=l[0:len(l)-1]
        print l
    elif(choice==3):
        break
    else:
        print "Invalid Choice!"
        
        
