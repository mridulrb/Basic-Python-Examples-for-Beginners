# File name: ...\\MyPythonXII\Unit1\PyChap05\floatq.py
# Program to perform queue operation on floating-point queue
Num = list() # A default queue using list() functon.
rear = front = -1 # Initializing the queue position
# Inserting element into a queue.
def Insert_Num(Num, rear):
    Ch = 'Y'
    while Ch == 'Y' or Ch == 'y'or Ch == 'Yes':
        fval = float(input("Enter a floating-point number: "))
        rear += 1
        Num.append(fval)   # Inserting floating-point number into queue.
        print ("Add more number <y/n>: ", end="")
        Ch = input()
        if Ch == 'N' or Ch == 'n' or Ch == 'No' or Ch == 'NO':
            break
    return rear

# Removing queue elements
def Delete_Num(Num, rear):
    Qlen = len(Num)   # Finds total elements in the queue. 
    if Qlen <= 0:   # Checks if queue is either empty or not.
        print ("Queue is empty")
    else:
        rear -= 1
        fval = Num.pop(0) # Removing from front of the queue.
        print("Value deleted from the queue is:", fval)
    return rear
    
# Showing queue elements
def Show_Nums(Num, rear):
    front = 0
    Qlen = len(Num)   # Finds total elements in the queue. 
    if Qlen <= 0:   # Checks if queue is either empty or not.
        print ("Queue is empty")
    else:        
        print("The queue elements are...")
        while front <= rear:  # Queue elements procesed.
            print(Num[front], end=" ")
            front += 1

while (True):
    front = -1
    print()
    print ('Q U E U E    O P E R A T I O N')
    print ('- - - - - - - - - - - - - - - -')
    print ('1. Adding number')
    print ('2. Removing number')
    print ('3. Showing numbers')
    print ('4. Exit')
    Opt = int(input( "Enter your option: "))
    print()
    if (Opt == 1) :
        # Insert operation of Queue
        rear = Insert_Num(Num, rear)
    elif (Opt == 2) :
        # Delete operation of queue
        rear = Delete_Num(Num, rear)        
    elif (Opt == 3) :
        # Traversing/Showing queue element
        Show_Nums(Num, rear)        
    elif (Opt == 4) :
        break
