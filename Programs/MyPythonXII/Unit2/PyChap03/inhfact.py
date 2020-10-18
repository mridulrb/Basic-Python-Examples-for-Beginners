# File name: ...\\MyPythonXII\Unit2\PyChap03\inhfact.py
# Demonstrating the class inheritance
class base:
    def __init__(self, cnt):
        self.counter = cnt
    def factorial(self):
        fact = 1
        for i in range(1, self.counter+1):
            fact = fact * i;
        print("The factorial value is:", fact)

class derived(base):
    def __init__(self, num):
        base.__init__(self, num)
    def displayFact(self):
        base.factorial(self)
    
num = int(input("Enter the value for factorial: "))
dr = derived(num)
dr.displayFact()
