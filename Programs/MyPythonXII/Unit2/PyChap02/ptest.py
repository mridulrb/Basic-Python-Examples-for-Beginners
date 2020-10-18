# File name: ...\\MyPythonXII\Unit2\PyChap02\ptest.py
class Friend:
    def __init__(self):
        self.Name = "Amit Rathore"
        self.__AotherName = "S. Narayanan"
    def printName(self):
        print(self.Name)
        print(self.__AotherName)
    def __inaccessible(self):
        print("You cann't access me.")

F = Friend()
print(F.Name)
#print(F.__AotherName)
F._Friend__inaccessible()
Friend()._Friend__inaccessible()
