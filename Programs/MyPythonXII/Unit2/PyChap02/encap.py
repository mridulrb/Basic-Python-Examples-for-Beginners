# File name: ...\\MyPythonXII\Unit2\PyChap02\encap.py
# Test of the behaviour of public, proctected and private members.
class DataEncap(object):
    # A class constructor
    def __init__(self, num1, num2, num3):
        self.public = num1
        self._protected = num2
        self.__private = num3

Val = DataEncap(10, 20, 30)
print("Public access number:", Val.public) # Accessible
print("Protected access number:", Val._protected) # Accessible
print("Private access number:", Val._DataEncap__private) # Accessible
print("Private access number:", Val.__private) # Not accessible

