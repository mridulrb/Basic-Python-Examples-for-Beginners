x=open("Article.txt","r")
upper=0
for i in x:
    for j in i:
        if(j.isupper()==True):
            upper=upper+1
print upper
x.close()
