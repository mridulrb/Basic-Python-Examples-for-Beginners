# File name: ...\\MyPythonXII\Unit1\PyChap03\matrixmlt.py
# Program to find the matrix multiplication
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

# Checking the number of columns of first matrix must be equal to the number of rows of 
# the second matrix.

if (c == r1):
    # Accept the Elements for matrix A
    print ("Enter elements for a %dx%d matrix A" % (r,c))
    for i in range(r):
        for j in range(c):
            print("Value for A[%d][%d]: " % (i, j), end='')
            A[i][j] = int(input())
    # Accept the Elements for matrix B
    print ("Enter elements for a %dx%d matrix B" % (r1,c1))
    for i in range(r1):
        for j in range(c1):
            print("Value for B[%d][%d]: " % (i, j), end='')
            B[i][j] = int(input())
    # Multiplying matrix A and B and storing in array C
    for i in range(r):
        for j in range(c1):
            for k in range(c):
                C[i][j] = C[i][j] + A[i][k] * B[k][j];            
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
    # Displaying the multiplication of two matrices.
    print("The multiplication result of two matrices C is : ")
    for i in range(r):
        print(" "*5, end="")
        for j in range(c1):
            print ("{0:^3}".format(C[i][j]), end='     ')
        print()
else:
    print("Order of two matrices is not correct ")
