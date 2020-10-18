# File name: ...\\MyPythonXII\Unit1\PyChap03\rcsum.py
# Program to find row sum and column sum of a matrix
# Declaration of a 3 x 4 matrix
Matrix =  [[0 for x in range(4)] for x in range(3)]
# Row sum function
def matrixRowSum(Matrix):
    for r in range(0, 3):
	Rsum = 0 
	for c in range(0, 4):
            Rsum = Rsum + Matrix[r][c]
	print("Sum of row %d is: %d" %(r+1, Rsum))
# Column sum function
def matrixColumnSum(Matrix):
    for r in range(0,4):
	Csum = 0
	for c in range(0,3):
            Csum = Csum + Matrix[c][r]
	print("Sum of column %d is: %d" %(r+1, Csum))

print("Enter the matrix elements")
for r in range(0, 3):
    print ("Enter values for row -> %d " %r)
    for c in range(0, 4):
        print ("Value for (%d,%d) -> " %(r, c), end=" ")
	Matrix[r][c] = int(input())
print ("The matrix is...")
for r in range(0, 3):
    print(" "*10, end="")
    for c in range(0, 4):
        print (Matrix[r][c], end="    ")
    print()
print()
matrixRowSum(Matrix)
matrixColumnSum(Matrix)
