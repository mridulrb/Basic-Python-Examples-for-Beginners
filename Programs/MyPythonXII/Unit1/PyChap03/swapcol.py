# File name: ...\\MyPythonXII\Unit1\PyChap03\swapcol.py
# Function to swap first column of an array with last column of a 4x4 matrix
def swapColumn(A):
    k = 3
    for i in range(4):
        tmp = A[i][0]
        A[i][0] = A[i][k]
        A[i][k] = tmp;
    print("Array after swapping is...")
    for i in range(4):
        print(" "*10, end="")
        for j in range(4):
            print(A[i][j], end="    ")
        print()
        
# Initializing the two dimensional array
A = [[2, 1, 4, 9],
     [1, 3, 7, 7],
     [5, 8, 6, 3],
     [7, 2, 1, 2]]
print("The original array is...")
for r in range(0, 4):
    print(" "*10, end="")
    for c in range(0, 4):
        print (A[r][c], end="    ")
    print()
print()

swapColumn(A)
