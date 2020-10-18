"Starting character of a line"
x=open("first.txt","r")
line=x.readlines()
print line
a=0
char=(raw_input("Enter starting character"))
for i in line:
    if(i[0]==char.upper()):
        a=a+1
print a
