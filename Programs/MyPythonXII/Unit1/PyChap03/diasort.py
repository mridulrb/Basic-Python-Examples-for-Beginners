# File name: ...\\MyPythonXII\Unit1\PyChap03\diasort.py

# Function to sort diagonal elements of a 4 x 4 matrix
def diagonalSort(A):
    # Sorting left diagonal
    for i in range(4):
        for j in range(4-1):
            if A[j][j] < A[j+1][j+1]:
                tmp = A[j][j]
                A[j][j] = A[j+1][j+1]
                A[j+1][j+1] = tmp;
    print("After diagonal sort, the matrix is...")
    for i in range(4):
        print(" "*10, end="")
        for j in range(4):
            print ("{0:^6}".format(A[i][j]), end=" ")
        print()


# Initializing the matrix
A = [[1, 5, 5, 8],
     [7, 45, 9, 11],
     [9, 6, 3, 10],
     [20, 6, 12, 82]]

print("The original matrix is...")
for r in range(0, 4):
    print(" "*10, end="")
    for c in range(0, 4):
        print ("{0:^6}".format(A[r][c]), end=" ")
    print()
print()
diagonalSort(A)
