print "Choose the option you want to use:"
print "A)Simple Interest"
print "B)Compund Interest"
print "C)Both"
choice=raw_input("Enter choice(Capital Letters)")
if(choice=="A"):
    p=input("Enter amount")
    r=input("Enter rate")
    t1=input("Enter years")
    t2=input("Enter months")
    t=(t1*12)+t2
    simpleinterest=(p*(r/12)*t)/100
    print simpleinterest
if(choice=="B"):
    p=input("Enter amount")
    r=input("Enter rate")
    t1=input("Enter years")
    t2=input("Enter months")
    m=input("Enter number of times interest is compounded per year")
    j=r/(100*m)
    if(t2!=0):
        t=t1+(t2/12)
    else:
        t=t1
    compoundinterest=p*((1+j)**(m*t))
    print compoundinterest
if(choice=="C"):
    p=input("Enter amount")
    r=input("Enter rate")
    t1=input("Enter years")
    t2=input("Enter months")
    tc=t1+(t2/12)
    ts=(t1*12)+t2
    m=input("Enter number of times interest is compounded per year")
    j=r/(100*m)
    if(t2!=0):
        t=t1+(t2/12)
    else:
        t=t1
    compoundinterest=p*((1+j)**(m*t))
    print compoundinterest
    simpleinterest=(p*(r/12)*ts)/100
    print simpleinterest
    j=r/(100*m)
