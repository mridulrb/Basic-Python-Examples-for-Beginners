# File name: ...\\MyPythonXII\Unit1\PyChap02\palindrome.py
# Program to check palindrome string
def reverse(list1, N):
    size = len(list1)
    i = 0
    while i < N:
        temp = list1[size-1-i]
        list1[size-1-i] = list1[i]
        list1[i] = temp
        i = i + 1
    
str1 = input("Enter any string: ")
str1 = str1.upper()
Rlist = list(str1)
N = len(str1) // 2
reverse(Rlist, N)
if list(str1) == Rlist:
    print("%s is a palindrome string" %str1)
else:
    print("%s is not a palindrome string" %str1)
