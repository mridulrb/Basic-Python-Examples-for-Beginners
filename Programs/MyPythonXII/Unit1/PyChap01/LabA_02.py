# File name: ...\\MyPythonXII\Unit1\PyChap01\LabA_02.py
# Program to perform mathematical calculations
add = sub = mult = div = 0
while True:
    print()
    print("Main Menu")
    print("------------------")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Quit")
    print("------------------")
    print("Enter you choice: ", end="")
    ch = input()
    if ch == '5':
        break
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    if ch == '1':
        add = x + y
        print("Sum of %0.2f and %0.2f is: %0.2f" %(x, y, add))
    elif ch == '2':
        sub = x - y
        print("Subtracting %0.2f from %0.2f is: %0.2f" %(y, x, sub))
    elif ch == '3':
        mult = x * y
        print("Multipying %0.2f with %0.2f is: %0.2f" %(x, y, mult))
    elif ch == '4':
        if x == 0 or y == 0:
            print("Both numbers must be positive")
        else:
            div = x / y
            print("Division of %0.2f by %0.2f is: %0.2f" %(x, y, div))
