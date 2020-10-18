s=raw_input("Enter string")
length=len(s)+1
for ch in range(1,length):
    print s[-ch]
for i in range(0,(length-1)):
    print s[i],"#",
