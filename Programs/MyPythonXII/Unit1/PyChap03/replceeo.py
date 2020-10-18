# File name: ...\\MyPythonXII\Unit1\PyChap03\replceeo.py

# Function to replace odd values with thrice their value
# and elements having even values with twice their value
def replaceEvenOdd(A):
    for i in range(len(A)):
        if (A[i] % 2 == 0):
            A[i] = A[i] * 2;    # Twice for even number
        else:
            A[i] = A[i] * 3;    # Thrice for even number
    print("The replaced array is: ")        
    for i in range(len(A)):
        print(A[i], end=" ")

# Initializing the array values
A = [3, 4, 5, 16, 9, 11, 8]
print("The initial array is: ")
for i in range(len(A)):
        print(A[i], end=" ")
print()
replaceEvenOdd(A)
