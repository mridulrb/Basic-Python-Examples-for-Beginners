# File name: ...\\MyPythonXII\Unit1\PyChap01\fact.py
# Program to find the factorial of a number
fact = i = 1
N = int(input("Enter any number to find factorial: "))
i = 1
while (i <= N):
    fact = fact * i
    i+=1
print ("The factorial of %d is %.2f" % (N, fact))
		
