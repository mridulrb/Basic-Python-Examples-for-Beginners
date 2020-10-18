# File name: ...\\MyPythonXII\Unit1\PyChap03\bsearch.py
# Program to search an element and its position in a list using binary search
Num = []    # An empty list

# Binary search function
def binarySearch(theArray, SearchVal) :
    # Start with the entire sequence of elements.
    low = 0
    pos = 'x'
    high = len(theArray) - 1
    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high :
        # Find the midpoint of the sequence.
        mid = (high + low) // 2
        # Does the midpoint contain the target?
        if theArray[mid] == SearchVal :
            pos = mid
            return True, pos
        # Or does the target precede the midpoint?
        elif SearchVal < theArray[mid] :
            high = mid - 1
        # Or does it follow the midpoint?
        else :
            low = mid + 1
    # If the sequence cannot be subdivided further, we're done.
    return False, pos

i = 0
n = int(input("Enter total numbers for an array: "))
while (i < n) :
    print ("Enter number %d: " % (i+1), end="")
    val = float(input())
    Num.append(val)   # adding number into list
    i += 1
Num.sort()  # List is sorted
print("Sorted array elements are...")
for i in range(0, n):
    print(Num[i])
# Searching an element and its position
pos = 0
Sval = float(input("\nEnter search element: "))

Flag, pos = binarySearch(Num, Sval)
if Flag == True:
    print("\nThe position of the element is: %d" %int(pos+1))
else:
    print("\nSearch element not found")
    
