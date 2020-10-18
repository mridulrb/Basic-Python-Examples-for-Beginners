# File name: ...\\MyPythonXII\Unit1\PyChap01\QEquation.py
# Program to calculate the roots of quadratic equation
import math
print ("For quadratic equation: \n")
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))
d = math.sqrt(b * b - 4 * a * c)
if (d < 0):
    print("Roots are imaginary")
if (d >= 0):
    r1 = (-b + d) / (2 * a);
    r2 = (-b - d) / (2 * a);
if ( d == 0):
    print("Roots are equal")        
print("First root is ", r1)
print("Second root is ", r2)



