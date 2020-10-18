# File name: ...\\MyPythonXII\Unit1\PyChap03\mlist.py
# Program to print a list from left to right and from right to left
Num = [4, 12, 2, 34, 17]	# A numeric list
print ("The original list elements are: ", end="")
for i in Num:
    print(i, end=" ")
ln = len(Num)
i = 0
ctr = -1
print()
print ("The reverse order list elements are: ", end="")
while i<=ln-1 :
    print (Num[ctr], end=" ")
    ctr-=1
    i+=1
