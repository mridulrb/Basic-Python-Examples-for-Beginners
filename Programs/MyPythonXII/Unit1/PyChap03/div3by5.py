# File name: ...\\MyPythonXII\Unit1\PyChap03\div3by5.py
# Function to find the sum of all the numbers which are either divisible
# by 3 or divisible by 5 in a two dimensional array (i.e., 5 x 5 matrix)
def DivBy3or5(A):
    Sum = 0
    for r in range(5):
        for c in range(5):
            if (A[r][c] % 5 == 0 or A[r][c] % 3 == 0):
                Sum += A[r][c];
    print ("The sum is:", Sum)
DivBy3or5(A = [[2, 3, 1, 5, 0],
                [7, 1, 5, 3, 1],
                [2, 5, 7, 8, 1],
                [0, 1, 5, 0, 1],
                [3, 4, 9, 1, 5]])
