# File name: ...\\MyPythonXII\Unit1\PyChap03\altsum.py
# Function to find the sum of elements from all alternate elements of a two-dimensional array
def alternateSum(A, row, col):
    C = 1
    Sum = 0
    for r in range(row):
        for c in range(col):
            if (C%2 != 0):
                Sum = Sum + A[r][c]
            C += 1
    return Sum
        
# Initializing the two dimensional array
A = [[4, 5, 1],
     [2, 8, 7],
     [9, 6, 3]]     
print("The original array is...")
for r in range(0, 3):
    print(" "*10, end="")
    for c in range(0, 3):
        print (A[r][c], end="    ")
    print()
print()
S = alternateSum(A, 3, 3)
print("Sum of alternate index positional values is:", S)
