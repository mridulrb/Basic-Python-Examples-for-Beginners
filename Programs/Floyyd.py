n=14
a,b,c=1,1,-1
while (a<=n):
    for j in range(b):
        if(a<=n):
            print a,
        else:
            break
        a+=1
    b+=1
    c+=1
    print    
a=a-b-c
while c>0:
    for k in range(1,c+1):
        d=k
        print a+k,
    print
    a-=d-1
    c-=1
    
        
