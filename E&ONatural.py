def sumavg(n):
    sumn=0
    even=0
    odd=0
    x=0
    o=0
    e=0
    for i in range(0,n+1):
        sumn=sumn+i
        x=x+1
        if(i%2==0):
            even=even+i
            e+=1
        if(i%2==1):
            odd=odd+i
            o+=1
    avg=sumn/x
    eavg=even/e
    oavg=odd/o
    print ("Natural no.s sum",sumn,"and average",avg)
    print ("Odd no.s sum",odd,"and average",o)
    print ("Even no.s sum",even,"and average",e)



           

    

    

