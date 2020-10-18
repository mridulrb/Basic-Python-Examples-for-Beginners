# File name: ...\\MyPythonXII\Unit1\PyChap02\countthe.py
# Loop to count number word: The or the
def countThe(String):
    count = 0
    print ("The line you entered....")
    Str = String.lower()    # Converted into lowercase string
    print (Str)
    LString = Str.split()   # Converted into a list of words
    print (LString)
    for i in range(len(LString)):
        if LString[i] == 'the' or LString[i] == 'the.' or \
           LString[i] == '.the' or LString[i] == '.the.':
            count += 1
    return (count)        
String = input("Enter a string: ")
tCount = countThe(String)
print ("Count of –The- or -the- in string is:", tCount)
