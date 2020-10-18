x=open("first.txt","r")
r=x.read()
print r
y=open("second.txt","w")
y.write(r[::-1])
y.close()
print "Reverse Content"
z=open("second.txt","r")
print z.read()
x.close()
z.close()
