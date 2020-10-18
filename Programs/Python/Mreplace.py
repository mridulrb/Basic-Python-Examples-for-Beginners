n="Jingle bells jingle bells jingle all the way"
w="bells"
v="stars"
for i in range (0,len(n)):
    if(n[i].isspace()==True):
        if(n[i:i+len(w)+1]==w):
            if(len(w)==len(v)):
                n[i:i+len(w)+1]=v
              
            else:
                m=n+(("")*(max(len(v),len(w))-min(len(v),len(w))))
                m[i:i+len(v)+1]=v
                for j in range(i+len(w)+1,len(m)):
                    m[i+len(v)+1:len(m)]=n[j]
            print m
print n
