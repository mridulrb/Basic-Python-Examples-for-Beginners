# File name: ...\\MyPythonXII\Unit1\PyChap03\dfarray.py
# Printing an array in different format
Num = []    # An empty list
# Declaration of three 10 x 10 matrices
D2AR =  [[0 for x in range(10)] for x in range(10)]

def ArrayFormat(Num):
    N = len(Num)
    for i in range(N):
        for j in range(N):
            if (i+j) >= N:
                D2AR[i][j] = 0 # Filling zeros
            else:
                D2AR[i][j] = Num[j] # Filling values
    print("If the 1-D array is : ...")
    for i in range(N):
        print (Num[i], end=" ")
    print()
    print("The 2-D array is : ...")
    for i in range(N):
        for j in range(N):
            print (D2AR[i][j], end= "  ")
        print()
i = 0
n = int(input("Enter total elements in array: "))

print("Enter elements in sorted order")
while (i < n) :
    print ("Enter number %d: " % (i+1), end="")
    val = int(input())
    Num.append(val)   # adding number into list
    i += 1
# Calling function
ArrayFormat(Num)
