string=raw_input("Enter string")
x=raw_input("Enter letter to be found")
y=1
for a in string:
    if (x!=a):
        y=y+1
    else:
        continue
print "Letter found at",y
