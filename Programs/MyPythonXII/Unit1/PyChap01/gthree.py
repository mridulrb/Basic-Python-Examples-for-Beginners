# File name: ...\\MyPythonXII\Unit1\PyChap01\gthree.py
# Program to print the greatest number between 3 numbers
fn = int(input("Enter first number: "))
sn = int(input("Enter second number: "))
tn = int(input("Enter third number: "))
if ((fn > sn) and (fn > tn)):
    print ("The greatest number is", fn)
elif (sn > tn) and (sn > fn):
    print ("The greatest number is", sn)
else:
    print ("The greatest number is", tn);
