# File name: ...\\MyPythonXII\Unit1\PyChap02\LabA_06.py
# Menu driven program to check palindrome number and perfect number.
import math
def digit_palindrome(N):
    String =""
    if N.isdigit():
        NumLength = len(N)
        TNum = int(N)
        while (TNum != 0):
            r_digit = TNum % 10
            String = String + str(r_digit)
            TNum = TNum//10
        if (N == String):
            print ("It is a palindrome number")
        else:
            print ("It is not a palindrome number")
def number_perfect(N):
    Sum = 0
    for i in range(1, N):
        # Check and sum of the factors, i.e., is i a factor of N
        if (N % i == 0):
            Sum = Sum + i
    if (Sum == N):
        print ("It is a perfect number")
    else:
        print ("It is not a perfect number")


while (True):
    print()
    print ("M A I N    M E N U")
    print ("- - - - - - - - - - -")
    print ("1. Palindrome number")
    print ("2. Perfect number")
    print ("3. Quit")
    print ("- - - - - - - - - - -")
    Opt = int(input( "Enter your option: "))
    print()
    if (Opt == 1) :
        N = input("Enter a number to check palindrome number: ")
        digit_palindrome(N)
    elif (Opt == 2) :
        N = int(input("Enter a number to check perfect number: "))
        number_perfect(N)
    elif (Opt == 3):
        break
