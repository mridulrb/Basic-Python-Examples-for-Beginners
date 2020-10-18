# File name: ...\\MyPythonXII\Unit1\PyChap01\sqcube.py
# Program to find the square and cube of numbers from 1 to 10 using table format.
print ("The table format is:")
print ("Number    Square    Cube")
for i in range(30):
    print ("-", end='')
print()
    
for x in range(1, 11):
    print('{0:2d} {1:10d} {2:10d}'.format(x, x*x, x*x*x))
for i in range(30):
    print ("-", end='')

