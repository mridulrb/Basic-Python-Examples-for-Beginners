# File name: ...\\MyPythonXII\Unit1\PyChap03\pmarks.py
# Program to print marks matrix

# Initializing the Marks
Marks = [[56, 43, 43, 65, 54],
	 [65, 54, 76, 34, 54],
	 [48, 67, 54, 56, 31]]

print ("The students marks before grace...")
for i in range(0, 3):
    print ("Student %d: " % int(i+1), end="")
    for j in range(0, 4):
        print (Marks[i][j], end="  ")
    print()
for i in range(0, 3):
    for j in range(0, 4):
        Marks[i][j] = Marks[i][j] + 10
print ("The students marks after grace...")
for i in range(0, 3):
    print ("Student %d: " % int(i+1), end="")
    for j in range(0, 4):
        print (Marks[i][j], end="  ")
    print()
        

