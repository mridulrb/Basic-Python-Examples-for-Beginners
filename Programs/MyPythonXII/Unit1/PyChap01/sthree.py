# File name: ...\\MyPythonXII\Unit1\PyChap01\sthree.py
# Program to print the smallest number between 3 numbers
Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))
Num3 = int(input("Enter third number: "))
if Num1 < Num2 :
    if Num1 < Num3 :
        smallest = Num1
    else:
        smallest = Num3
else:
    if Num2 < Num3 :
        smallest = Num2
    else:
        smallest = Num3
print ("The smallest number is:", smallest);
