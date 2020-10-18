# File name: ...\\MyPythonXII\Unit1\PyChap05\custq.py
custQ = list() # A default queue using list() functon.
rear = front = -1 # Initializing the queue position
# Inserting customer data
def Insert_Q(custQ, rear):
    Ch = 'Y'
    while Ch == 'Y' or Ch == 'y'or Ch == 'Yes':
        custID = int(input("Enter Customer ID: "))
        custName = input("Enter Customer name: ")
        rear += 1
        CData = (custID, custName) # Creating a tuple
        custQ.append(CData) # A tuple added into a list        
        print ("Insert more customer <y/n>: ", end="")
        Ch = input()
        if Ch == 'N' or Ch == 'n' or Ch == 'No' or Ch == 'NO':
            break
    return rear

# Removing customer data
def Delete_Q(custQ, rear):
    Clen = len(custQ)   
    if Clen <= 0:   
        print ("Customer queue is empty")
    else:
        rear -= 1
        custID, custName = custQ.pop(0) 
        print("Customer ID %d and Customer name: %s deleted" % (custID, custName))
    return rear
    
# Showing customer data
def Show_Q(custQ, rear):
    front = 0
    Plen = len(custQ)   # Finds total customers in queue
    if Plen <= 0:   # Checks if the customer queue is either empty or not.
        print ("No cusomer in queue")
    else:        
        print ("Customer information")
        print ("="*46)
        print ("{0:^15} {1:<20}".format("Customer ID", "Customer Name"))
        print ("-"*46)        
        while front <= rear:  # Queue elements procesed.
            custID, custName = custQ[front]
            print ("{0:^15} {1:<20}".format(custID, custName))
            front += 1

while (True):
    front = -1
    print()
    print ('P A S S E N G E R    O P E R A T I O N')
    print ('- - - - - - - - - - - - - - - - - - - -')
    print ('1. Insert Customer data')
    print ('2. Delete Customer data')
    print ('3. Show Customers')
    print ('4. Exit')
    Opt = int(input( "Enter your option: "))
    print()
    if (Opt == 1) :
        # Insert operation of Queue
        rear = Insert_Q(custQ, rear)
    elif (Opt == 2) :
        # Delete operation of queue
        rear = Delete_Q(custQ, rear)        
    elif (Opt == 3) :
        # Traversing/Showing customers
        Show_Q(custQ, rear)        
    elif (Opt == 4) :
        break
