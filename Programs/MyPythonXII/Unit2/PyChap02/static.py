# File name: ...\\MyPythonXII\Unit2\PyChap02\static.py
# Demonstrates static method in a class
class Static:
    p = 100
    q = 120
    # A static method
    def Static_Method1():
        # initializing two local variables
        a, b = 20, 45.60
        _Sum = a + b # Result in a local variable
        print ("The sum of %.2f and %.2f is: %.2f" % (a, b, _Sum))
    # A parameterized static method
    def Static_Method2(x, y = 100):
        # initializing two local variables
        a, b = x, y
        z = Static.p + Static.q
        _Sum1 = a + b # Result in a local variable
        print ("The sum of %.2f and %.2f is: %.2f" % (a, b, _Sum1))        
    # A class method
    def Class_Method(self):
        # Calling a static method through class name inside a class method
        Static.Static_Method2(50, 70)
        
# Creating a class object
Sobj = Static() 
print ("Static_method1() output")
# Calling two static methods outside the class through the class name
Static.Static_Method1()
print ("Static_method2() output")
Static.Static_Method2(40)
print ("Static_method2() output through class method")
# Calling a class method in main through class object
Sobj.Class_Method()

