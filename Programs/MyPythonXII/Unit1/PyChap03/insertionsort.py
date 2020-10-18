# File name: ...\\MyPythonXII\Unit1\PyChap03\insertionsort.py
# Program to arrange an array in ascending order of insertion sort method
Num = [] # An empty array

# Sorts a sequence in ascending order using the insertion sort algorithm.
def insertionSort(Num):
    n = len(Num)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n) :
        # Save the value to be positioned.
        value = Num[i]
        # Find the position where value fits in the ordered part of the list.
        pos = i
        while pos > 0 and value < Num[pos - 1] :
            # Shift the items to the right during the search.
            Num[pos] = Num[pos - 1]
            pos -= 1
        # Put the saved value into the open slot.
        Num[pos] = value

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
insertionSort(Num)
print()
print("The sorted list...")
for i in range(0, n):
    print(Num[i], end=" ")

