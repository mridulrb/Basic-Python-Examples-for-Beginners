q=[]
front=-1
rear=-1
while True:
    print "    1)Insertion"
    print "    2)Deletion"
    print "    3)Display"
    print "    4)Exit"
    choice=input("Enter choice:")
    if(choice==1):
        data=input("Enter data:")
        q.append(data)
        if(q==[]):
            front+=1
            rear+=1
        else:
            rear+=1
    elif(choice==2):
        if(q==[]):
            print "Underflow condition"
        else:
            q=list(q[1:len(q)])
            print q
            front-=1
    elif(choice==3):
        print q[0],"<--Front"
        for i in range(1,len(q)-1):
                print q[i]
        print q[len(q)-1],"<--Rear"
    elif(choice==4):
        break
