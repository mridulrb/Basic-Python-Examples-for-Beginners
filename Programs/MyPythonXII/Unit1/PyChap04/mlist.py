# File name: ...\\MyPythonXII\Unit1\PyChap04\mlist.py
# Menu driven program for list manipulation
Num = list() # Creating an empty list

# Adding element into list
def add_element(ctr):
    ctr += 1
    Ch = 'Y'
    while Ch == 'Y' or Ch == 'y'or Ch == 'Yes':
        print ("Enter value for position %d: " % (ctr), end="")
        val = input()
        Num.append(val)   # adding number into list
        print ("Do you want to add more...<y/n>: ", end="")
        Ch = input()
        ctr += 1
        if Ch == 'N' or Ch == 'n' or Ch == 'No' or Ch == 'NO':
            break

# Insert function
def insert_element(n):
    print ("Insert Options")
    print ("--------------")
    print ("1 - At the beginning")
    print ("2 - At the end")
    print ("3 - At the Middle")
    print ("4 - At position")
    print ("Enter your option: ", end="")
    opt = int(input())
    if opt == 1:
        Num.insert(0, n) # Value inserted at beginning
    elif opt == 2:
        Num.append(n)   # Inserted at end
    elif opt == 3:
        Mid = int(len(Num)/2) # convert into int
        Num[Mid:Mid] = [n] # Assign an iterable value
        print('Value inserted...')
    elif opt == 4:
        pos = int(input("Enter the insert position: "))
        pos -= 1 # The actual index position for a list is index - 1
        if pos <= len(Num):
            Num.insert(pos, n) # value inserted at position
        else:
            print("Insert position is out of range")

# Show list elements
def show_element():
    print("The list is:...")
    for i in range(0, len(Num)):
        print(Num[i], end="  ")

# Delete list elements
def delete_element(n):
    Flag = 0
    for i in range(len(Num)):
        if Num[i] == n:
            del (Num[i])
            Flag = 1
            break
    if Flag == 0:
        print("Element does not found in list")
    else:
        print("Successfully deleted")
    
Opt = 0
while (True):
    print()
    print (' M A I N   M E N U')
    print ('- - - - - - - - - -')
    print ('1. Add element')
    print ('2. Insert element')
    print ('3. Delete element')
    print ('4. Show elements')
    print ('5. Quit')
    print ('- - - - - - - - - -')
    Opt = int(input( "Enter your option: "))
    print()
    if (Opt == 1) :
        ctr = len(Num)
        add_element(ctr)
    elif (Opt == 2) :
        # If list has more than one element then insertion is possible
        if len(Num) > 1:
            n = input("Enter inserted value: ")
            insert_element(n)
        else:
            print ('List need more than equal to 2 elements before insert')
            x = input('Press <Enter> key')
    elif (Opt == 3) :
        if not Num:
            print("List is empty")
        else:
            n = input("Enter the element which you want to delete: ")
            delete_element(n)
    elif (Opt == 4) :
        if not len(Num):	# Checks if there is no element in list
            print ("List is empty")
        else:
            show_element()
    elif (Opt == 5) :
        break
        
