name=raw_input("Enter Name:")
a=""
l=name.split(" ")
for i in range(len(l)-1):
    b=l[i][0].upper()
    a=a+b+"."
c=l[len(l)-1][0].upper()
d=c+l[len(l)-1][1:len(l[len(l)-1])]
a+=d
print a
