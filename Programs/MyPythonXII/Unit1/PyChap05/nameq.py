# File name: ...\\MyPythonXII\Unit1\PyChap05\nameq..py
# Insert and delete operation in a dynamically allocated Queue
# containing  names of students.	
stdName = list() # A student name list
rear = front = -1 # Initializing the queue position
# Function to insert student name into a queue.
def Insert_Name(stdName, rear):
    Ch = 'Y'
    while Ch == 'Y' or Ch == 'y'or Ch == 'Yes':
        Name = input("Enter student name: ")
        rear += 1
        stdName.append(Name)   # Name inserted
        print ("Insert more name...<y/n>: ", end="")
        Ch = input()
        if Ch == 'N' or Ch == 'n' or Ch == 'No' or Ch == 'NO':
            break
    return rear

# Function to delete student name from a queue.
def Delete_Name(stdName, rear):
    totStd = len(stdName)   # Finds total student in queue
    if totStd <= 0:   # Student name queue empty
        print ("Queue is empty")
    else:
        rear -= 1
        Name = stdName.pop(0) # Removing from front of the queue.
        print("Name deleted from the queue is:", Name)
    return rear
    
# Showing queue elements
def Show_Names(stdName, rear):
    front = 0
    totStd = len(stdName)   # Finds total student in queue
    if totStd <= 0:   # Student name queue empty
        print ("Queue is empty")
    else:        
        print("Student names are...")
        while front <= rear:  # Queue elements procesed.
            print(stdName[front], end=" ")
            front += 1

while (True):
    front = -1
    print()
    print ('Student Name Operation')
    print ('- - - - - - - - - - - - - - - -')
    print ('1. Insert studet')
    print ('2. Delete student')
    print ('3. Shows Students')
    print ('4. Exit operation')
    Opt = int(input( "Choose your option: "))
    print()
    if (Opt == 1) :
        # Insert operation of Queue
        rear = Insert_Name(stdName, rear)
    elif (Opt == 2) :
        # Delete operation of queue
        rear = Delete_Name(stdName, rear)        
    elif (Opt == 3) :
        # Showing student names
        Show_Names(stdName, rear)        
    elif (Opt == 4) :
        break
