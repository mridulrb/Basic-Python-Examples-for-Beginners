n="A"
l=ord(n)
for i in range(1,27):
    for j in range(i):
        print chr(l+j),
    print

for k in range(l,92):
    for m in range(l,k+1):
        print chr(m),
    print 

a="a"
b=ord(a)
for i in range(1,27):
    for j in range(i):
        print chr(b+j),
    print
for k in range(b,123):
    for m in range(b,k+1):
        print chr(m),
    print 

for i in range(26):
    for j in range(i+1):
        print chr(65+i),
    print

for i in range(26):
    for j in range(i+1):
        print chr(97+i),
    print


