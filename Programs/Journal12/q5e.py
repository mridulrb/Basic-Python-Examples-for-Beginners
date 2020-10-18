import random
import bisect
l=[]
for i in range(9):
    r=random.randint(1,100)
    pos=bisect.bisect(l,r)
    bisect.insort(l,r)
print l
