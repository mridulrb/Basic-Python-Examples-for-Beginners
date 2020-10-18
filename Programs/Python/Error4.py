try:
    x=float(input("Enter your number"))
    inverse=1.0/x
except ValueError:
    print "you should have given either int or float"
except ZeroDivisionError:
    print "Infinity"
finally:
    print "there may or may not be an exception"
"""
if input is:
    6
    0
    6.7
    "a"
"""
