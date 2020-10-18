# File name: ...\\MyPythonXII\Unit1\PyChap03\lhalf.py
# Function Lower_half which prints the lower half of the array
def Lower_half(A):
    k = 0
    print ("The original array is")
    for r in range(5):
        print(" "*10, end="")
        for c in range(5):
            print ("{0:^3}".format(A[r][c]), end=" ")
        print()
    print()
    print ("The lower half of the array is")
    for i in range(len(A)):
        print(" "*10, end="")
        j = 0
        while j<=k:
            print ("{0:^3}".format(A[i][j]), end=" ")
            j += 1
        print()
        k += 1
Lower_half(A = [[2, 3, 1, 5, 0],
                [7, 1, 5, 3, 1],
                [2, 5, 7, 8, 1],
                [0, 1, 5, 0, 1],
                [3, 4, 9, 1, 5]])
