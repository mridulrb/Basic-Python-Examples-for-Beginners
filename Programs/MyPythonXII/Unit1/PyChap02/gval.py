# File name: ...\\MyPythonXII\Unit1\PyChap02\gval.py
# Accessing global variable inside a function.
# Create the x variable and set to 44
x =44
def VarScope(Var):
    x = 22
    print ("The value of x is:", x)

def AccessGval():
    print ("Before the function call x is:", x)
    print ("Inside VarScope function")
    VarScope(x)
    print ("After the function call x is:", x)
AccessGval()
                  
