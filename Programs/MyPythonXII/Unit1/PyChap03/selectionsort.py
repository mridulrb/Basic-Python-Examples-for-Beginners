# File name: ...\\MyPythonXII\Unit1\PyChap03\selectionsort.py
# Program to arrange an array in ascending order of selection sort method
Num = [] # An empty array

# Sorts a sequence in ascending order using the selection sort algorithm.
def selectionSort(Num):
    n = len(Num)
    for i in range( n - 1 ):
        # Assume the ith element is the smallest.
        smallNdx = i
        # Determine if any other element contains a smaller value.
        for j in range( i + 1, n ):
            if Num[j] < Num[smallNdx] :
                smallNdx = j
        # Swap the ith value and smallNdx value only if the smallest value is
        # not already in its proper position. Some implementations omit testing
        # the condition and always swap the two values.
        if smallNdx != i :
            tmp = Num[i]
            Num[i] = Num[smallNdx]
            Num[smallNdx] = tmp

i = 0
n = int(input("Enter the number of elements in array: "))
while (i < n) :
    print ("Enter number %d: " % (i+1), end="")
    val = int(input())
    Num.append(val)   # adding number into list
    i += 1

print()
print("The original list...")
for i in range(0, n):
    print(Num[i], end=" ")
selectionSort(Num)
print()
print("The sorted list...")
for i in range(0, n):
    print(Num[i], end=" ")

