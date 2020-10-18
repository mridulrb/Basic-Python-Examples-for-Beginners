print ("Valid or Invalid Date") 
year=input("Enter year")
month=input("Enter month in number")
date=input("Enter date")
if(month>12 or month<0):
    print ("Invalid date")
else:
    if(month==1 and 3 and 5 and 7 and 8 and 10 and 12):
        if(date>31 or date<1):
            print ("Invalid date")
        else:
            print ("Valid date")
    if(month==4 and 6 and 9 and 11):
        if(date>30 or date<1):
            print ("Invalid date")
        else:
            print ("Valid date")
    if(year%4==0):
        if(month==2):
            if(date>29 or date<1):
                print ("Invalid date")
            else:
                print ("Valid date")
    if(year%4!=0):
        if(month==2):
            if(date>28 or date<1):
                print ("Invalid date")
            else:
                print ("Valid date")
