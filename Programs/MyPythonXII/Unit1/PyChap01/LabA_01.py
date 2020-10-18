# File name: ...\\MyPythonXII\Unit1\PyChap01\LabA_01.py
# Program to find monthly instalment of a loan
import math
T = 12 * 6 # Total months of loan
R = 9.5    # Loan interest rate (fixed)
P = 500000 # Principal amount
# Using the formula, M = [A/(1-B)] x P
A = R / 1200 # Amount
B = (1/(1 + A)**T)
M = math.ceil((A / (1 - B)) * P)
print("Monthly installment is: %.2f" % (M))
