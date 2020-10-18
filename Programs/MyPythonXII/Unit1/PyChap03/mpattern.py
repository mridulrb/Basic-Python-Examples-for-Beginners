# File name: ...\\MyPythonXII\Unit1\PyChap03\mpattern.py
# Program to print a pattern

A =  [[0 for x in range(10)] for x in range(10)]
i = j = b = c = 0

while(i<10) :
    j = 0
    while(j<10)	:
        if (i!=0 and j==0) :
            c = i - 1
            b = A[c][j]
            b = b + 1
        A[i][j] = b
        if(b==9) :
            b = b - 10
        b = b + 1
        j = j + 1        
    i += 1
i = j = 0
while(i<10) :
    j = 0
    while(j<10)	:
        print(A[i][j], end = "   ")
        j += 1
    print()
    i += 1
    
    

        
