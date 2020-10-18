# File name: ...\\MyPythonXII\Unit1\PyChap01\sseries.py
# This program finds the sum of series
n = int(input("Enter the value of n => "))
x = int(input("Enter the value of x => "))
p = 1
sum = 1
for i in range(2, n+1):
    f = 1
    for j in range(1, i+1):
        f = f * j
    p = p * x
    p1 = p/f
    sum = sum + p1;
print ("Sum of series is –>%d " %(sum))
         
