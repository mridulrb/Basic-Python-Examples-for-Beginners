# File name: ...\\MyPythonXII\Unit1\PyChap01\LabA_04.py
# Menu drive program for :
# Special number, Armstrong number, Prime number and Automorphic number.
import math
while (True):
    print()
    print ("M A I N    M E N U")
    print ("- - - - - - - - - - -")
    print ("1. Special number")
    print ("2. Armstrong number")
    print ("3. Prime number")
    print ("4. Atomorphic number")
    print ("5. Quit")
    print ("- - - - - - - - - - -")
    Opt = int(input( "Enter your option: "))
    print()
    if (Opt == 1) :
        N = int(input("Enter a number to check special number: "))
        N1 = N
        Rem = Sum = 0
        while (N1 > 0):
            Rem = N1 % 10
            N1 = N1 // 10  #Floor division
            # Factorial of digit (Remainder)
            F = 1
            for i in range(1, Rem+1):
                F = F * i
            Sum = Sum + F
        if (N == Sum):
            print ("It is a special number.")
        else
            print ("It is not a special number.")
    elif (Opt == 2) :
        N = int(input("Enter a number to check armstrong number: "))
        N1 = N
        Rem = Sum = 0
        while (N1 > 0):
            Rem = N1 % 10
            N1 = N1 // 10  #Floor division
            Sum = Sum + math.pow(Rem, 3)
        if (N == Sum):
            print ("It is an armstrong number.")
        else:
            print ("It is not an armstrong number.")
    elif (Opt == 3) :
        Opt = 0
        N = int(input("Enter a number to check prime number: "))
        for i in range(2, N):
            if (N % i == 0):
                Opt = 1
                break
            i = i + 1
        if (Opt == 1):
            print("It is not a prime number")
        else:
            print("It is a prime number")
    elif (Opt == 4):
        N = int(input("Enter a number to check automorphic number: "))
        N1 = N
        Ctr = Rem = Sum = 0
        while (N1 > 0): # Counting total digits in input number
            Rem = N1 % 10
            N1 = N1 // 10  #Floor division
            Ctr += 1
        SqrNum = N * N # Square of the input number
        LastDigit = count = 0
        for i in range(1, Ctr+1):
            Rem = SqrNum % 10
            LastDigit = LastDigit * 10 + Rem
            SqrNum = SqrNum // 10
            count += 1
        Ctr = Rem = Ld = 0
        for i in range(1, count+1):
            Rem = LastDigit % 10
            Ld = Ld * 10 + Rem
            LastDigit = LastDigit // 10
        if (N == Ld):
            print("It is an automorphic number")
        else:
            print("It is not an automorphic number")

    elif (Opt == 5):
        break

