# File name: ...\\MyPythonXII\Unit1\PyChap04\stack.py
# Program to perform stack operations.
Stack = list() # A default stack using list() functon.
top = -1 # To know the current index position in Stack.
# Adding element into a stack.
def Push_element(Stack, top):
    Ch = 'Y'
    while Ch == 'Y' or Ch == 'y'or Ch == 'Yes':
        val = input("Enter the value to be added in the stack: ")
        Stack.append(val)   # Adding element into list.
        top += 1 # It check the total number of addition
        print ("Do you want to add more...<y/n>: ", end="")
        Ch = input()
        if Ch == 'N' or Ch == 'n' or Ch == 'No' or Ch == 'NO':
            break
    return top

# Removing stack elements
def Pop_element(Stack, top):
    slen = len(Stack)   # Finds total elements in the stack. 
    if slen <= 0:   # Checks if stack is empty or not.
        print ("Stack is empty")
    else:        
        val = Stack.pop() # Removing from top of the stack.
        top = top - 1
        print("Value deleted from stack is", val)
    return top
    
# Showing stack elements
def Show_element(Stack, top):
    slen = len(Stack) # Finds total elements in the stack.
    if slen <= 0:    # Checks if stack is empty or not.
        print ("Stack is empty")
    else:        
        print("The stack elements are...")
        i = top
        while (i >= 0):  # Stack elements process in reverse order.
            print(Stack[i])
            i -= 1

while (True):
    print()
    print ('S T A C K    O P E R A T I O N')
    print ('- - - - - - - - - - - - - - - -')
    print ('1. Adding elements to a stack')
    print ('2. Removing elements from a stack')
    print ('3. Showing elements of a stack')
    print ('4. Exit from stack operation')
    Opt = int(input( "Enter your option: "))
    print()
    if (Opt == 1) :
        # Push operation of stack - Adding element at top of the stack
        top = Push_element(Stack, top)
    elif (Opt == 2) :
        # Pop operation of stack - Deleting element from top of the stack
        top = Pop_element(Stack, top)
    elif (Opt == 3) :
        Show_element(Stack, top)
    elif (Opt == 4) :
        break
