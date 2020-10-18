# File name: ...\\MyPythonXII\Unit1\PyChap03\summatrix.py
# Program to add two matrices

# Declaration of three 10 x 10 matrices
A =  [[0 for x in range(10)] for x in range(10)]
B =  [[0 for x in range(10)] for x in range(10)]
C =  [[0 for x in range(10)] for x in range(10)]

print("Enter the number of Rows of matrix A: ", end='')
r = int(input())
print("Enter the number of Columns of matrix A: ", end='')
c = int(input())

print("Enter the number of Rows of matrix B: ", end='')
r1 = int(input())
print("Enter the number of Columns of matrix B: ", end='')
c1 = int(input())

# Before accepting the Elements Check if no of
#   rows and columns of both matrices is equal 

if (r == r1 and c == c1):
    # Accept the Elements for matrix A
    for i in range(r):
        for j in range(c):
            print("Enter the element A[%d][%d]: " % (i, j), end='')
            A[i][j] = int(input())
    # Accept the Elements for matrix B
    for i in range(r):
        for j in range(c):
            print("Enter the element B[%d][%d]: " % (i, j), end='')
            B[i][j] = int(input())
    # Addition of two matrices
    for i in range(r):
        for j in range(c):
            C[i][j] = A[i][j] + B[i][j]
    # First matrix
    print("Matrix A:")
    for i in range(r):
        print(" "*5, end="")
        for j in range(c):
            print("{0:^3}".format(A[i][j]), end='     ')
        print()
    print("Matrix B:")
    for i in range(r):
        print(" "*5, end="")
        for j in range(c):
            print("{0:^3}".format(B[i][j]), end='     ')
        print()            
    # Print out the Resultant Matrix C
    print("The Addition of two Matrices C is : ")
    for i in range(r):
        print(" "*5, end="")
        for j in range(c):
            print ("{0:^3}".format(C[i][j]), end='     ')
        print()
else:
    print("Order of two matrices is not same ")
