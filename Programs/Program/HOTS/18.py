n=raw_input("enter line")
k=n
y=""
y=y+(n[0].upper())+"."
for i in range(1,len(n)):
    if(n[i]==" "):
        a=k[i+1].upper()
        y=y+a+"."
        break
for j in range(i+1,len(n)):
        if (n[j]==" "):
            y=y+n[j+1].upper()
            for k in range(j+2,len(n)):
                y=y+n[k]
print y
