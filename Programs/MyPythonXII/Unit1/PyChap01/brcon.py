# File name: ...\\MyPythonXII\Unit1\PyChap01\brcon.py
N = int(input("Enter N --> "))
for i in range(0, N+1, 1): # Start loop from 0 to N (N included)
    if i**2 == N:       # Test if i**2 is equal to N
        break           # if it is stop counting
    else:
        if i % 5 == 0:  # Test if i is a multiple of 5
            continue    # if it is, move to next value
        print (i, end=' ')
