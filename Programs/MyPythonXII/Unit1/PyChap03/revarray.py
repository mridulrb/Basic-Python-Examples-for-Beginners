# File name: ...\\MyPythonXII\Unit1\PyChap03\revarray.py

# Function to display an initialize array in reverse order.
def reverseArray(A):
    N = len(A)
    j = N - 1
    for i in range(int(N/2)): # int(N/2): converting float to int
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp
        j -= 1
    print("The reverse array is: ")
    for i in range(N):
        print(A[i], end=" ")

# Initializing the array values
A = [4, 2, 5, 1, 7, 6, 8, 12, 10]
print("The initial array is: ")
for i in range(len(A)):
        print(A[i], end=" ")
print()
reverseArray(A)
