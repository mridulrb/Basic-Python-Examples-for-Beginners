# File name: ...\\MyPythonXII\Unit1\PyChap03\mlist.py
# Modifying a list index values
Num = [ ]	# An empty list
print ("Enter 5 values:")
for i in range (5) :
    print("Enter value %d: " % int(i+1), end="")
    v = int(input())
    Num.append(v)
print ("List before modification:")
for i in range(5):
    print(Num[i], end="  ")
# Modifying by multiplying 5 with each list index value
for i in range(5):
    Num[i] = Num[i] * 10
print ("\nList after modification:")
for i in range(5):
    print(Num[i], end="  ")
