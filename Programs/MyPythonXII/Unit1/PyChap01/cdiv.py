# File name: ...\\MyPythonXII\Unit1\PyChap01\cdiv.py
# This program finds the greatest common divisor of two numbers.
x = int(input("Enter first number  –> "))
y = int(input("Enter second number  –> "))
r1 = 0
rem = x % y
while (rem != 0):
    x = y
    y = rem
    rem = x % y    
print ("Greatest common divisor is –>", y)

