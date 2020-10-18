# File name: ...\\MyPythonXII\Unit1\PyChap03\transpose.py

# Program to perform transpose of a matrix
MAT1 = [[0 for x in range(3)] for x in range(4)] 
MAT = [[4, 5, 8, 6],
       [2, 3, 2, 4],
       [7, 6, 4, 6]]
print ("The matrix is...")
for r in range(0, 3):
    for c in range(0, 4):
        print (MAT[r][c], end="  ")
    print()
print()
# Transferring row data into column form
for r in range(0, 4):
    for c in range(0, 3):
        MAT1[r][c] = MAT[c][r]
				
print ("The resultant matrix is...")
for r in range(0, 4):
    for c in range(0, 3):
        print (MAT1[r][c], end="  ")
    print()
