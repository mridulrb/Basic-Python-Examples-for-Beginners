# File name: ...\\MyPythonXII\Unit1\PyChap03\mergesort.py
# Program to merge two sorted array in ascending order using merge sort method
Range3 = [] # An empty array

# Merges two sorted lists to create and return a new sorted list.
def mergeSortedLists(Range1, Range2) :
    # Create the new list and initialize the list markers.
    Range3 = list()
    a = 0
    b = 0
    # Merge the two lists together until one is empty.
    while a < len(Range1) and b < len(Range2) :
        if Range1[a] < Range2[b]:
            Range3.append(Range1[a])
            a += 1
        else:
            Range3.append(Range2[b])
            b += 1
    # If Range1 contains more items, append them to Range3.
    while a < len(Range1) :
        Range3.append(Range1[a])
        a += 1
    # Or if Range2 contains more items, append them to Range3.
    while b < len(Range2) :
        Range3.append(Range2[b])
        b += 1
    return Range3

i = 0
# Initializing two sorted lists
Range1 = [2, 8, 15, 23, 37]
Range2 = [4, 6, 15, 20]
Range3 = mergeSortedLists(Range1, Range2)
print ('Range 1 is:', Range1)
print ('Range 2 is:', Range2)
print ('Sorted Range 3 is:', mergeSortedLists(Range1, Range2))
