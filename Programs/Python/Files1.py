x=open("first.txt","r")
files=x.read()
a=[]
b=[]
c='a','e','i','o','u'
for i in files:
    if(i.isspace()==False):
        a=a+[i]
    elif(i.isspace()):
        b=b+[''.join(a)]
        del a[0:len(a)]
print b
y=open("second.txt","w")
for j in b:
    if(j.startswith(c)):
        y.write(j+'\n')
y.close()
z=open("second.txt","r")
for k in z:
    print k,
x.close()
y.close()
z.close()

        
        
        
    
    
