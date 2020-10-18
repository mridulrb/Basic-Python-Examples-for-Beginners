# File name: ...\\MyPythonXII\Unit1\PyChap03\shiftn.py
# Initializing an array to shift numbers
A = [3, -5, 1, 3, 7, 0, -15, 3, -7, -8]
print("The original array...")
for i in range(len(A)):
    print(A[i], end=" ")
print()
i = 0
# Function to shift negative and positive numbers.
def swap(A):
    ln = len(A)
    j = 0
    for i in range(10):
        j = i 
        if (A[j] < 0):
            t = A[j]
            while (j >= 0):
                A[j] = A[j-1]
                j -= 1
                if (A[j] < 0):
                    break;
            A[j+1] = t            
swap(A)
print("Array after shifting...")
for i in range(len(A)):
    print(A[i], end=" ")

