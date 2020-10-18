# File name: ...\\MyPythonXII\Unit1\PyChap03\exchalf.py
# Function to exchange first half of an array with second half
A = [2, 4, 1, 6, 7, 9, 23, 10]
def Exchange(A):
    N = len(A)
    print ("The initial array is:", A)
    for i in range(int(N/2)): # int(N/2): converting float to int
        Tmp = A[i]
        A[i] = A[(int(N/2)) + i]
        A[int(N/2) + i] = Tmp  
    print ("The exchanged array is", A)
Exchange(A)
