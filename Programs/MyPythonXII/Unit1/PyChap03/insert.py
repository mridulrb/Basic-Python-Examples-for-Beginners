# File name: ...\\MyPythonXII\Unit1\PyChap03\insert.py
# Menu driven program to perform insert operation
theList = list() # Creating a default list/array

# Insert at beginning
def insertAtBeginning(theList, insVal):
    theList.insert(0, insVal)  # Inserted at 0th position
    
# Insert at middle position
def insertAtMiddle(theList, insVal):
    Mid = int(len(theList)/2) # convert into int
    theList[Mid:Mid] = [insVal] # Assign an iterable value    

# Insert at end
def insertAtEnd(theList, insVal):
    theList.append(insVal)   # Value appended

# Insert at position
def insertAtPosition(theList, insVal, InsPos):
    theList.insert(InsPos, insVal)   

# Show array elements
def show_element(theList):
    ctr = len(theList)
    if ctr > 0:
        print("The array is:...")
        for i in range(0, len(theList)):
            print(theList[i], end="  ")
    else:
        print ("List is empty")

Opt = 0
while (True):
    print()
    print (' M A I N   M E N U')
    print ('- - - - - - - - - -')
    print ('1. Insert element at beginning')
    print ('2. Insert element at middle')
    print ('3. Insert element at end')
    print ('4. Insert at a position')
    print ('5. Show elements')
    print ('6. Quit')
    print ('- - - - - - - - - -')
    Opt = int(input( "Enter your option: "))
    print()
    if (Opt == 6):
        break
    if (Opt == 1) :
        Val = input("Enter the value to be inserted: ")
        insertAtBeginning(theList, Val)
    elif (Opt == 2) :
        Val = input("Enter the value to be inserted: ")
        # if array has more than one element then insertion is possible
        ctr = len(theList)
        if ctr > 1:
            insertAtMiddle(theList, Val)
        else:
            print("The array has less than two elements")
            print("Insertion at middle not possible")
    elif (Opt == 3) :
        Val = input("Enter the value to be inserted: ")
        insertAtEnd(theList, Val)
    elif (Opt == 4) :
        Val = input("Enter the value to be inserted: ")
        Pos = int(input("Enter the position: "))
        ctr = len(theList)
        if ctr == 0:    # If there is no element in array
            insertAtPosition(theList, Val, ctr) # insert at 0th index position
        elif Pos > 0 and Pos < ctr:
            insertAtPosition(theList, Val, Pos-1)
            # Pos-1 because, the array index starts at 0.
        else:
            print("Position output of index")
    elif (Opt == 5) :
        show_element(theList)
