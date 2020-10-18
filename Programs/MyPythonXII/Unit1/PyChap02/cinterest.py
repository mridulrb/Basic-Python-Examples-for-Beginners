# File name: ...\\MyPythonXII\Unit1\PyChap01\CInterest.py
# Program to find compound interest

def CompoundAmt(P, r, n, t = 6):
    """
    Apply the compound interest formula to produce the final amount.
    """
    A = P * ((1 + r/n) ** (n*t))
    return A  # This is new, and makes the function fruitful.


def main():
    P = 1500    # principal amount (initial investment)
    r = 4.3/100 # annual nominal interest rate (as a decimal)
    n = 4     # number of times the interest is componded per year
    t = 6   # t = number of years
    Famount = CompoundAmt(P, r, n, t)
    print("At the end of %i years the balance will be %.2f" % (t, Famount))

main()
