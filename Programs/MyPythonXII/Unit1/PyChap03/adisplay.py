# File name: ...\\MyPythonXII\Unit1\PyChap03\adisplay.py
# Function to display all alternate elements from a two-dimensional array
def alternateValue(A, row, col):
    print ("The original array is...")
    for r in range(row):
        print(" "*10, end="")
        for c in range(col):
            print ("{0:^6}".format(A[r][c]), end=" ")
        print()
    print()
    counter = 0
    print("The alternate elements are:")
    for i in range(row):
        for j in range(col):
            if (counter % 2 == 0):
                print(A[i][j], end=" ")
            counter = counter + 1
# Main program
A =  [[0 for x in range(10)] for x in range(10)]
print("Enter number of rows ", end='')
row = int(input())
print("Enter number of columns ", end='')
col = int(input())
print("Enter array values")
for i in range(0, row):
    for j in range(0, col):
        print ("Value for (%d,%d) -> " %(i, j), end=" ")
        A[i][j] = int(input())
alternateValue(A, row, col)
