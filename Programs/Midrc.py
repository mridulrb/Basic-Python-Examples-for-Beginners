n=list(input("enter 2d list"))
if ((len(n)%2)!=0):
        midrow=(len(n)-1)/2
        print "middle row",n[midrow],
if ((len(n)%2)==0):
        midrow1=(len(n)/2)
        print "middlerow1",n[midrow1-1],
        print "middlerow2",n[midrow1],
if ((len(n)%2)!=0):
    print "middle column"
    for i in range(0,len(n)):
        y=list()
        for j in range(0,len(n[i])):
            midcol=(len(n)-1)/2
            y=y+[n[j][midcol]]
    print y,
print
if ((len(n)%2)==0):
    print "middle columns"
    for i in range(0,len(n)):
        t=list()
        r=list()
        for j in range(0,len(n[i])):
            midcol1=(len(n)/2)
            t=t+[n[j][midcol1-1]]
            r=r+[n[j][midcol1]]
    print t,
    print r,
print
