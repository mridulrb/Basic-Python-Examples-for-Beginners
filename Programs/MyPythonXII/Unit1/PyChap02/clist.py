# File name: ...\\MyPythonXII\Unit1\PyChap02\clist.py
my_list =[] # Empty list
for i in range (5) :
    print ("Enter value ", i+1, end=': ')
    userInput = int(input())
    my_list.append(userInput) # Appends element at the last of the list
print ("The list is:",my_list)
