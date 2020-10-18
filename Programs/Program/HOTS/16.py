string=raw_input("Enter string")
iscount=0
for i in range(0,len(string)):
    if(string[i]=='i' and string[i+1]=='s'):
        iscount=iscount+1
    else:
        continue
print iscount

