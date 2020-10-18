# File name: ...\\MyPythonXII\Unit2\PyChap02\private.py
# Demonstrates private variables and methods
class testMe:
    __Sum = 0 # A private class variable
    # Constructor called when creating an object of class type
    def __init__(self, n1, n2):
        self.num1 = n1 # A public attribute
        self.__num2 = n2 # A private attribute
        # Result stored in a public attribute
        self.Sum = self.num1 + self.__num2   # or self.Sum = n1 + n2
    def __Aprivate_method(self):
        # initializing two local variables
        a = 20
        b = 45.60
        self.__Sum = a + b # Result in a private class variable
        # Using private class variable in private method
        print ("The sum of %.2f and %.2f is: %.2f" % (a, b, self.__Sum))
    def Apublic_method(self):
        self.__Aprivate_method()
        # Calling private class variable in public method
        print ("The sum of %d and %d is: %d" % (self.num1, self.__num2, self.Sum))
        
# Creating a class object with three parameterized values
Cobj = testMe(40, 50) # Constructor method called
# Calling the public class method using instance object
Cobj.Apublic_method()



