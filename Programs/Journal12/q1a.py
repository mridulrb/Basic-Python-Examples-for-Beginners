phonedict={}
x=input("Enter no. of records:")
for i in range(x):
    name=raw_input("Enter Name:")
    phonedict[name]=raw_input("Enter Telephone no.:")
while True:
    print "         1)Search for a Telephone no."
    print "         2)Search for a name"
    print "         3)Display a Telephone no."
    print "         4)Display a name"
    print "         5)Add a record"
    print "         6)Modify a Telephone no."
    print "         7)Modify a name"
    print "         8)Delete a record"
    print "         9)Display"
    print "         10)Exit"
    choice=input("Enter choice:")
    if(choice==1):
         if(phonedict=={}):
            print "Dictionary is empty."
         else:
            name=raw_input("Enter Name:")
            for i in phonedict:
                if(i==name):
                    print "Name:",i,"Telephone no.:",phonedict[i]
            if(phonedict.has_key(name)==False):
                print "Record not found!"
    elif(choice==2):
         if(phonedict=={}):
            print "Dictionary is empty."
         else:
            teleno=raw_input("Enter Telephone no.:")
            value=phonedict.values()
            for i in phonedict:
                if(phonedict[i]==teleno):
                    print "Name:",i,"Telephone no.:",phonedict[i]
                elif(phonedict[i] not in value):
                    print "Record not found!"
    elif(choice==3):
        if(phonedict=={}):
            print "Dictionary is empty."
        else:
            name=raw_input("Enter Name:")
            for i in phonedict:
                if(i==name):
                    print "Name:",i,"Telephone no.:",phonedict[i]
            if(phonedict.has_key(name)==False):
                    print "Record not found!"
    elif(choice==4):
        if(phonedict=={}):
            print "Dictionary is empty."
        else:
            value=phonedict.values()
            teleno=raw_input("Enter Telephone no.")
            for i in phonedict:
                if(phonedict[i]==teleno):
                    print "Name:",i,"Telephone no.:",phonedict[i]
                if(phonedict[i] not in value):
                    print "Record not found!"
    elif(choice==5):
        name=raw_input("Enter Name:")
        phonedict[name]=raw_input("Enter Telephone no.:")
    elif(choice==6):
         if(phonedict=={}):
            print "Dictionary is empty."
         else:
            name=raw_input("Enter Name:")
            for i in phonedict:
                if(i==name):
                    phonedict[i]=raw_input("Enter Telephone no.:")
            if(phonedict.has_key(name)==False):
                print "Record not found!"
    elif(choice==7):
         if(phonedict=={}):
            print "Dictionary is empty."
         else:
            value=phonedict.values() 
            teleno=raw_input("Enter Telephone no.:")
            for i in phonedict:
                if(phonedict[i]==teleno):
                    del phonedict[i]
                    name=raw_input("Enter Name:")
                    phonedict[name]=teleno
                elif(phonedict[i] not in value):
                    print "Record not found!"
    elif(choice==8):
        if(phonedict=={}):
            print "Dictionary is empty."
        else:
            name=raw_input("Enter Name:")
            if(phonedict.has_key(name)==False):
                print "Record not found!"
            else:
                del phonedict[name]    
    elif(choice==9):
         if(phonedict=={}):
            print "Dictionary is empty."
         else:
             for i in phonedict:
                 print i,":-",phonedict[i]
    elif(choice==10):
        break
    else:
        print "Invalid choice!"
