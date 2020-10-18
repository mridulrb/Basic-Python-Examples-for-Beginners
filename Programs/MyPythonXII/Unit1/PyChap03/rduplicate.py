# File name: ...\\MyPythonXII\Unit1\PyChap03\rduplicate.py

# Function to remove duplicate elements in an array
def removeDuplicate(A):
    for i in range(len(A)-1):
        j = i + 1
        while j < (len(A)):
            if A[i] == A[j]:  # Checks for repeated elements
                A.pop(j)
            j += 1
    if (A[-1] == A[-2]): # check and remove if last two elements are same
        del A[-1]
            
    print("After removing duplicate elements, the array is...")
    for i in range(len(A)):
        print(A[i], end=" ")
        

# Initializing the array values
A = [4, 2, 5, 1, 9, 7, 3, 2, 4, 8, 12, 8, 3, 12, 7]
print("The initial array is: ")
for i in range(len(A)):
        print(A[i], end=" ")
print()
removeDuplicate(A)
