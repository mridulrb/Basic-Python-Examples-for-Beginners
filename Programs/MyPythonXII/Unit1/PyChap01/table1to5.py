# File name: ...\\MyPythonXII\Unit1\PyChap01\table1to5.py
# Program to find table from 1 to 5 using nested for loop
for i in range(1, 6):
    t = 1
    print ("Math table: ", i)
    print ()
    for j in range(1, 11):
        t = i * j
        print ("%d * %d = %d" % (i, j, t))
    print ()    
