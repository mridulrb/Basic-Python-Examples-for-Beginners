# File name: ...\\MyPythonXII\Unit1\PyChap05\queue.py
# Program to perform queue operation.
Queue = list() # A default queue using list() function.
rear = front = -1 # Initializing the queue position
# Inserting element into a queue.
def Insert_Queue(Queue, rear):
    Ch = 'Y'
    while Ch == 'Y' or Ch == 'y'or Ch == 'Yes':
        val = input("Enter the value to be added into the queue: ")
        rear += 1
        Queue.append(val)   # Adding element into queue list.
        print ("Do you want to add more...<y/n>: ", end="")
        Ch = input()
        if Ch == 'N' or Ch == 'n' or Ch == 'No' or Ch == 'NO':
            break
    return rear

# Removing queue elements
def Remove_Queue(Queue, rear):
    Qlen = len(Queue)   # Finds total elements in the queue. 
    if Qlen <= 0:   # Checks if queue is empty or not.
        print ("Queue is empty")
    else:
        rear -= 1
        val = Queue.pop(0) # Removing from front of the queue.
        print("Value deleted from the queue is:", val)
    return rear
    
# Showing queue elements
def Show_Queue(Queue, rear):
    front = 0
    Qlen = len(Queue)   # Finds total elements in the queue. 
    if Qlen <= 0:   # Checks if queue is empty or not.
        print ("Queue is empty")
    else:        
        print("The queue elements are...")
        while front <= rear:  # Queue elements processed.
            print(Queue[front], end=" ")
            front += 1

while (True):
    front = -1
    print()
    print ('Q U E U E    O P E R A T I O N')
    print ('- - - - - - - - - - - - - - - -')
    print ('1. Adding elements to a queue')
    print ('2. Removing elements from a queue')
    print ('3. Showing elements of a queue')
    print ('4. Exit from queue operation')
    Opt = int(input( "Enter your option: "))
    print()
    if (Opt == 1) :
        # Insert operation of Queue - Adding element at rear of the queue
        rear = Insert_Queue(Queue, rear)
    elif (Opt == 2) :
        # Delete operation of queue - Deleting element at front of the queue
        rear = Remove_Queue(Queue, rear)        
    elif (Opt == 3) :
        # Traversing/Showing queue element
        Show_Queue(Queue, rear)        
    elif (Opt == 4) :
        break
