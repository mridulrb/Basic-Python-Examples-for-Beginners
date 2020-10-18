#String Reverse
line=raw_input("Enter text:")
l=line.split(" ")
a=""
for i in range(len(l)):
    b=l[i]
    c=""
    for j in range(len(b)-1,-1,-1):
        c=c+b[j]
    a+=c+" "
print a   
        
