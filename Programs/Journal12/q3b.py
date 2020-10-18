x=open("Poem.txt","r")
to=0
the=0
for i in x:
    l=i.split(" ")
    for j in l:
        if(j=="to" or j=="To"):
            to+=1
        elif(j=="the" or j=="The"):
            the+=1
print "TO-",to
print "THE-",the
x.close()
