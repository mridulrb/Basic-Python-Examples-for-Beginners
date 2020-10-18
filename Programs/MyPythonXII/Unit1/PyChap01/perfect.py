# File name: ...\\MyPythonXII\Unit1\PyChap01\perfect.py
# Program to find the perfect numbers between 1 and 500
import math
i, u, sum = 1, 1, 0
while i<=500 :  #start of first loop.
    while u<=500 : #start of second loop.
        if u<i:
            if i%u == 0 :
                sum = sum + u; # End of if statement
        u+=1 #End of second loop
    if(sum==i):
        print ("%d is a perfect number." % i)
    i+=1
    u, sum =1, 0
