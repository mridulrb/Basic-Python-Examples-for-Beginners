# File name: ...\\MyPythonXII\Unit1\PyChap03\rowm.py
# Initializing the two dimensional array
A = [[20, 40, 10],
     [40, 50, 30],
     [60, 30, 20],
     [40, 20, 30]]
    
print("The original array is...")
for r in range(0, 4):
    print(" "*10, end="")
    for c in range(0, 3):
        print (A[r][c], end="    ")
    print()
print()
# Function to calculate the multiplication of row elements
def rowMultiplication(A):
    for i in range(4):
        mult = 1
        for j in range(3):
            mult = mult * A[i][j]
        print("Product of row %d = %d" % (i+1, mult))
rowMultiplication(A)
