# File name: ...\\MyPythonXII\Unit1\PyChap03\bubblesort.py
# Program to arrange an array in ascending order of bubble sort method
Num = [] # An empty array

# Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort(Num):
    n = len(Num) # Calculate the length of array
    # Perform n-1 bubble operations on the sequence
    for i in range(n) :
        # Bubble the largest item to the end.
        for j in range(n - 1) :
            if Num[j] > Num[j + 1] : # swap the j and j+1 item.
                tmp = Num[j]
                Num[j] = Num[j + 1]
                Num[j + 1] = tmp

i = 0
n = int(input("Enter total numbers for an array: "))
while (i < n) :
    print ("Enter number %d: " % (i+1), end="")
    val = int(input())
    Num.append(val)   # adding number into list
    i += 1

print()
print("The original list...")
for i in range(0, n):
    print(Num[i], end=" ")
bubbleSort(Num)
print()
print("The sorted list...")
for i in range(0, n):
    print(Num[i], end=" ")

