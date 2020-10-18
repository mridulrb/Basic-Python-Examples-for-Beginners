x=open("first.txt","r")
y=open("Home.txt","w")
st=x.readline()
for i in st:
    y.write(i.strip())
z=open("Home.txt","r")
s=z.read()
for j in s:
    print j,
