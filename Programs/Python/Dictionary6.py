months={"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}
print months
while 1:
    print "Select an option"
    print "1)Find the no of days"
    print "2)Print the months"
    print "3)Print the months with 31 days"
    print "4)Print months sorted by days"
    choice=int(raw_input("Enter choice"))
    if(choice==1):
        month=raw_input("Enter month")
        print months[month]
    elif(choice==2):
        key=months.keys()
        key.sort()
        print key
    elif(choice==3):
        for i in months:
            if(int(months[i])==31):
                print i
    elif(choice==4):
        thirtyone={}
        thirty={}
        twentyeight={}
        for i in months:
            if(int(months[i])==31):
                thirtyone[i]=31
            elif(int(months[i])==30):
                thirty[i]=30
            elif(int(months[i])==28):
                 twentyeight[i]=28
        print thirtyone
        print thirty
        print twentyeight
