# File name: ...\\MyPythonXII\Unit1\PyChap03\slargest.py
# Program to find the second largest element in an array
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
# Find second largest element
def secondLargest(Num):
    print()
    n = len(Num) # Calculate the length of array
    ctr = -1
    slarge = flag = 0
    opt = 'N'
    # Loop to check all the numbers equal or not
    for i in range(n-1):
        if Num[i] == Num[i+1]:
            opt = 'Y'
        else:
            opt = 'N'   # Any case when nos. are different then break
            break;
    if opt == 'N':
        # Second largest statements
        for i in range(n):
            if Num[ctr] != Num[ctr-1]:
                slarge = Num[ctr-1]
                flag = 1
                break
            else:
                ctr -= 1
    return flag, slarge, opt        

i = 0
n = int(input("Enter total numbers for an array: "))
while (i < n) :
    print ("Enter number %d: " % (i+1), end="")
    val = int(input())
    Num.append(val)   # adding number into list
    i += 1
print()
print("The original list...")
for i in range(len(Num)):
    print(Num[i], end=" ")
# Calling sorting function
bubbleSort(Num)
print()
print("The sorted list...")
for i in range(len(Num)):
    print(Num[i], end=" ")
# Calling second largest function
Flag, Slarge, Opt = secondLargest(Num)
print()
if Opt == 'N' and Flag == 1:
    print("The second largest element is:", Slarge)
else:
    print("Array elements are all equal numbers")
