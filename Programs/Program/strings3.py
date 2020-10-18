line=raw_input("Enter string")
x=0
for a in line:
    if(a in ' '):
        x=x+1
    else:
        continue
print "Number of words",x+1


