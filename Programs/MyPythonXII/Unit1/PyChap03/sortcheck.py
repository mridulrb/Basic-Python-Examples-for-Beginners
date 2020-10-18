# File name: ...\\MyPythonXII\Unit1\PyChap03\sortcheck.py
# Function to check either an array is sorted or not.
def check(A):
    flag = 0;
    # Checking for ascending order
    for j in range(len(A)-1):
        if(A[j] < A[j+1]):
            flag = 1            
        else:
            flag = 0 # for no order
            break
    if (flag == 1):
        return flag
    # Checking for descending order
    for j in range(len(A)-1):
        if (A[j] > A[j+1]):
            flag = -1
        else:
            flag = 0 # for no order
            break
    return flag

# Input 10 values
A = list()
for i in range(10):
    print ("Enter value ", i+1, ": ", end="")
    val = int(input())
    A.append(val)
s = check(A)
if (s == 1):
    print("Arranged in ascending order")
elif (s == -1):
    print("Arragned in descending order")
elif (s == 0):
    print("Not arranged")

