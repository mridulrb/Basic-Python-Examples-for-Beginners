f=open("first.txt","r")
g=open("second.txt","w")
for i in f:
    i=i+" "
    x=0
    k=len(i)
    while x<k:
        p=i.find(" ",x,k)
        if p!=-1:
            if i[x] in "aeiou":
                for a in range(x,p):
                    new+=i[a]
                new+=" "
                x=p+1
            else:
                    x=p+1
        else:
            break
        g.write(new)
g.close()
f.close()
