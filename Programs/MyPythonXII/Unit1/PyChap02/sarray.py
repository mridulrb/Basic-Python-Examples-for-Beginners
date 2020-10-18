# File name: ...\\MyPythonXII\Unit1\PyChap02\sarray.py
# Demonstration for average of ten different students total marks
marray = []
tot = avg = 0
for i in range(10):
    print ("Enter mark %d ->" % int(i+1), end=' ')
    mark = int(input())
    marray.append (mark)
    tot = tot + mark
avg = tot / 10
print ("Marks are:", end=' ')
for i in range(10):
    print (marray[i], end=" ")
print ("Average is :", avg)
		
