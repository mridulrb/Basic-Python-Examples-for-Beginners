# File name: ...\\MyPythonXII\Unit2\PyChap02\strmethod.py
# A class using __str__() method
class SumTwo:
    # Constructor called when creating an object of class type
    def __init__(self, x, y):
        # Creating instance variables
        self.a = x
        self.b = y
    def __str__(self):
        '''Display self as a string.'''
        return ('%d' % (self.a + self.b))
    

# Creating a class object with three parameterized values
Result = SumTwo(10, 20)
print ("The sum is:", Result)
