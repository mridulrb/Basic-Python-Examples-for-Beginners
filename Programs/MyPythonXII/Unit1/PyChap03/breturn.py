# File name: ...\\MyPythonXII\Unit1\PyChap03\breturn.py
# Program to search an element and its position in a list using binary search
Num = []    # An empty list

# Binary search function with returning value
def returnValueSearch(Num, val) :
    low = 0
    high = len(Num) - 1
    while low <= high :
        mid = (high + low) // 2
        if Num[mid] == val :
            pos = mid
            return 1
        elif val < Num[mid] :
            high = mid - 1
        else :
            low = mid + 1
    return 0

i = 0
n = int(input("Enter total elements in array: "))
print("Enter elements in sorted order")
while (i < n) :
    print ("Enter number %d: " % (i+1), end="")
    val = float(input())
    Num.append(val)   # adding number into list
    i += 1
# Searching an element and its position
pos = 0
Sval = float(input("\nEnter search element: "))
Flag = returnValueSearch(Num, Sval)
if Flag == 1:
    print("The search value found")
else:
    print("\nSearch element not found")
    
