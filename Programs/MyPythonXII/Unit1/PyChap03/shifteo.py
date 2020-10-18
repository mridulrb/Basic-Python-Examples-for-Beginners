# File name: ...\\MyPythonXII\Unit1\PyChap03\shifteo.py
A = [3, 2, 1, 7, 6, 3]
B = [9, 3, 5, 6, 2, 8, 10]
C = list()
# Function MIX() produces a third array 
def MIX(A, B, C):
    m = len(A)
    n = len(B)
    i = j = 0
    # Copying even numbers from first array A to third array C
    for i in range(m):
        if A[i] % 2 == 0:
            C.append(A[i])
    # Copying even numbers from second array B to third array C
    while (j < n):
        if B[j] % 2 == 0:
            C.append(B[j])
        j += 1
    # Copying odd numbers from first array A to third array C
    for i in range(m):
        if A[i] % 2 != 0:
            C.append(A[i])
    # Copying odd numbers from second array B to third array C
    j = 0
    while (j < n):
        if B[j] % 2 != 0:
            C.append(B[j])
        j += 1
    print ("The first array A is:", A)
    print ("The second array B is:", B)
    print ("The third array C is:", C)
    
MIX(A, B, C)

