# File name: ...\\MyPythonXII\Unit1\PyChap01\swap.py
# This program swaps two numbers without using third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("After swapping a is –> %d" %(a))
print("After swapping b is –> %d" %(b))
   
