# File name: ...\\MyPythonXII\Unit1\PyChap03\lsearch.py
# Program to search an element and its position in a list
Num = []    # An empty list

# Linear search function
def linearSearch(theArray, SearchVal) :
    n = len(theArray)
    pos = 'x'
    for i in range(n) :
        # If the target is in the ith element, return True and search position (pos)
        if theArray[i] == SearchVal:
            pos = i
            return True, pos
    return False, pos # If not found, return False.

i = 0
n = int(input("Enter total numbers for an array: "))
while (i < n) :
    print ("Enter number %d: " % (i+1), end="")
    val = float(input())
    Num.append(val)   # adding number into list
    i += 1

# Searching an element and its position
pos = 0
Sval = float(input("\nEnter search element: "))

print("The original list...")
for i in range(0, n):
    print(Num[i], end=" ")
Flag, pos = linearSearch(Num, Sval)
if Flag == True:
    print("\nPosition of the search element in array is: %d" %int(pos+1))
else:
    print("\nSearch element not found")
    
