n=[input("Enter elements")]
x=len(n)
empty=list()
while True:
    import random
    i=random.randint(0,x)
    empty=empty+[n[i]]
print empty
