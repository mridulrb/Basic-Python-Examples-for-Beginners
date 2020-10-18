# File name: ...\\MyPythonXII\Unit1\PyChap03\gletter.py

# Function to print greater letter its index+1 time.
def printGLetter(str1, str2):
    S1 = len(str1)
    S2 = len(str2)
    if S1 == S2:
        for i in range (S1):
            j = i + 1   # index + 1 times
            if str1[i] > str2[i]:
                print(str1[i]*j)
            elif str1[i] < str2[i]:
                print(str2[i]*j)
            elif str2[i] > str1[i]:
                print(str2[i]*j)
            elif str2[i] < str1[i]:
                print(str1[i]*j)
str1 = 'Shyam'
str2 = 'Mohan'
print(str1, "   ", str2)
printGLetter(str1, str2)

