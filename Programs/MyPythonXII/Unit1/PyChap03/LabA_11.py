# File name: ...\\MyPythonXII\Unit1\PyChap03\LabA_l1.py
# Create and sum the positive and negative numbers.
PosNum = [] # An empty array
NegNum = [] # An empty array
n = int(input("Enter how many numbers you want? "))
i = 0
if n > 0:
    print ("Enter number both +ve and -ve numbers...")
    while (i < n) :
        print ("Enter number %d " % (i+1), end="")
        Num = float(input())
        if Num > 0:
            PosNum.append(Num)   # adding number into +ve list
        else:
            NegNum.append(Num)   # adding number into -ve list
        i += 1
    SPos = SNeg = 0
    print("The +ve number list is:", PosNum)
    print("The -ve number list is:", NegNum)
    # Sum of +ve numbers
    for i in range(0, len(PosNum)):
        SPos = SPos + PosNum[i]
    # Sum of -ve numbers
    for i in range(0, len(NegNum)):
        SNeg = SNeg + NegNum[i]
    print ("Sum of +ve number(s):", SPos)
    print ("Sum of -ve number(s):", SNeg)
else:
    print ("Input is not correct")
