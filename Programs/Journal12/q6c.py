s=[]
top=len(s)-1
while True:
    print "    1)Push"
    print "    2)Pop"
    print "    3)Peek"
    print "    4)Display"
    print "    5)Exit"
    choice=input("Enter choice:")
    if(choice==1):
        book_no=input("Enter Book no.:")
        book_name=raw_input("Enter Book name:")
        s+=[[book_no,book_name]]
        top+=1
    elif(choice==2):
        if(s==[]):
            print "Underflow Condition"
        else:
            print s.pop(),"<--Deleted Element"
            top-=1
    elif(choice==3):
        if(s==[]):
            print "Underflow Condition"
        else:
            print s[len(s)-1],"<--Top"
    elif(choice==4):
        if(s==[]):
            print "Underflow Condition"
        else:
            print s[top],"<--Top"
            top-=1
            while(top!=-1):
                print s[top]
                top-=1
    elif(choice==5):
        break
            
