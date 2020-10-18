# File name: ...\\MyPythonXII\Unit1\PyChap03\getarray.py
# Function to transfer the content of one array ALL[] to two different arrays
# The Odd[] array should contain odd positions (1, 3, 5, …) of ALL[]
# and Even[] array should contain even positions (0, 2 4, …) of ALL[].
def transferEvenOdd(All, Even, Odd):
    print ("The array All is:", All)
    for i in range(len(All)):
        if All[i] % 2 == 0:
            Even.append(All[i])
        else:
            Odd.append(All[i])
    print ("The array Even is:", Even)
    print ("The array Odd is:", Odd)

All = [12, 34, 56, 67, 89, 90, 43, 12, 87, 34]
Odd = list()
Even = list()
transferEvenOdd(All, Even, Odd)

