string=raw_input("Enter string")
x=0
for a in string:
    if(a not in ' '):
        x=x+1
    else:
        continue
print "Number of characters:",x
