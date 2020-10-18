a=list(input("Enter elements"))
a.sort()
b=list(input("Enter elements"))
b.sort()
a.extend(b)
c=a
c.sort()
print c
