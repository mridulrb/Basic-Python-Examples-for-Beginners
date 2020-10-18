x=open("Poem.txt","r")
y=open("article.txt","w")
for i in x:
    l=i.split(" ")
    for j in l:
        if(j[0] in 'aeiou' or j[0] in 'AEIOU'):
            y.write(j+" ")
x.close()
y.close()
y=open("article.txt","r")
for i in y:
    print i
y.close()
