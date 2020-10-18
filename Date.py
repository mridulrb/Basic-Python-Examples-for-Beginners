print "Valid or Invalid Date"
x=raw_input("enter date in DD/MM/YYYY : ")
if (len(x)!=10):
    print "enter in DD/MM/YYYY format"
else:    
    d1=x[0]
    d2=x[1]
    date=10*int(d1)+int(d2)
    m1=x[3]
    m2=x[4]
    month=10*int(m1)+int(m2)
    y1=x[6]
    y2=x[7]
    y3=x[8]
    y4=x[9]
    year=1000*int(y1)+100*int(y2)+10*int(y3)+int(y4)
    a=[1,3,5,7,8,10,12]
    b=[4,6,9,11]
    if (month<=12 and month>=1):
        if (month in a):
            if (date>=1 and date<=31):
                print "Valid Date"
            else:
                print "Invalid Date"
        elif (month in b):
            if (date>=1 and date <=30):
                print "Valid Date"
            else:
                print "Invalid Date"
        elif (month==2):
            if (year%4==0 and date>=1 and date<=28):
                print "Valid Date"
            elif (year%4!=0 and date>=1 and date<=27):
                print "The date is valid."
            else:
                print "Invalid Date"
    else:
        print "Invalid Date"



