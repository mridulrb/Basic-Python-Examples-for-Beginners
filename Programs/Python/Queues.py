que=[]
front=-1
rear=-1
while True:
    print "QUEUE OPERATIONS"
    print "1. insert"
    print "2. delete"
    print "3. PEEK"
    print "4. DISPLAY"
    print "5. EXIT"
    c=input("Enter your choice")
    if c==1:
        if front==-1:
            print " inserting first element"
            front=front +1
        x=input("enter data  to be pushed")
        rear=rear+1
        que+=[x]
    elif c==2:
        if front==-1:
            print "UNDERFLOW"
        elif front==rear:
                print " only one element in queue"
                print que[front] , " is deleted"
                front=rear=-1
        else:
            print que[front] , " is deleted"
            front=front +1
    elif c==3:
        if front==-1:
            print "UNDERFLOW"
        else:
            print "The first element is ",que[front]
    elif c==4:
         if front==-1:
            print "UNDERFLOW"
         elif front==rear:
             print que[rear],  " <----FRONT & REAR "
         else:
             print que[rear],   "<--  REAR"
             for i in range (rear-1,front,-1):
                 print que[i]
             print que[front],  "<--FRONT"
    elif c==5:
        break
    else:
        print "Invalid Choice"
