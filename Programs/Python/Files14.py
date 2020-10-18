x=open("first.txt","r")
y=open("second.txt","w")
for line in x: 
    for word in line.split():
        if(word[0] in 'aeiou'):
            y.write(word+'\n')
        else:
            continue
x.close()
y.close()
z=open("second.txt","r")
for i in z:
    print i,
z.close()
               
               
