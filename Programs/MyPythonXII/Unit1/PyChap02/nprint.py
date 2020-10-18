# File name: ...\\MyPythonXII\Unit1\PyChap02\nprint.py
# Program to print name character times.
name = input("Enter your name: ")
length = len(name)
ctr = 0
newName = ""
# loop to delete space from the name
while ctr <= length-1:
    if name[ctr].isspace():
        pass
    else:
        newName = newName+name[ctr]
    ctr+=1

# printing name character times
nlength = len(newName)  # length after deleting space
print ("Your name will print %d times." % int(nlength))
for i in range(nlength):
    print (name)
