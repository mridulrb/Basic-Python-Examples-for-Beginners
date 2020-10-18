# File name: ...\\MyPythonXII\Unit1\PyChap03\swap10.py
# Function to swap the array value which is divisible by 10 with next value.
def swapM10(A, Size):
    i = 0
    while (i < Size):
        if (A[i]%10 == 0):
            tmp = A[i]
            A[i] = A[i+1]
            A[i+1] = tmp
            i = i + 2 # if swapped skip 2 position to the index
        else:
            i += 1
    print ("The array after swap is:")
    for i in range(len(A)):
        print (A[i], end=" ")
    
A = [90, 56, 45, 20, 34, 54]
print ("The array is:")
for i in range(len(A)):
    print (A[i], end=" ")
print()
swapM10(A, len(A))


