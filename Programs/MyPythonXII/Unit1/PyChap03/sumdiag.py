# File name: ...\\MyPythonXII\Unit1\PyChap03\sumdiag.py
# Function to display the sum of diagonals of a 6x6 matrix
def sumDiagonals(Matrix):
    print ("The matrix is...")
    for r in range(6):
        print(" "*10, end="")
        for c in range(6):
            print ("{0:^6}".format(Matrix[r][c]), end=" ")
        print()
    print()
    LeftDSum = RightDSum = 0
    # Sum of diagonal left to right
    for r in range(6):
        for c in range(r, r+1):
            LeftDSum = LeftDSum + Matrix[r][c]
    # Sum of diagonal right to left
    c = 5
    for r in range(6):
        RightDSum = RightDSum + Matrix[r][c]
        c-=1

    print ("\t\tSum of left diagonal is :", LeftDSum)
    print ("\t\tSum of right diagonal is :", RightDSum)
    
sumDiagonals(Matrix = [[6, 11, 12, 24, 5, 3],
                       [5, 8, 7, 1, 5, 2],
                       [8, 6, 8, 2, 7, 3],
                       [3, 5, 9, 2, 5, 2],
                       [4, 8, 2, 8, 4, 3],
                       [4, 16, 2, 8, 7, 9],])
