# File name: ...\\MyPythonXII\Unit1\PyChap02\pasf.py
n = int(input("Enter the number of students:"))
data = {} # here we will store the data
languages = ('English', 'Physics', 'Chemistry', 'Maths', 'Computer') #all languages
for i in range(0, n): #for the n number of students
    #Get the name of the student
    name = input('Enter the name of the student %d: ' % (i + 1))
    marks = []
    for x in languages:
        #Get the marks for languages
        marks.append(int(input('Enter marks of %s: ' % x)))
        data[name] = marks
    for x, y in data.items():
        total = sum(y)
        print ("%s 's total marks %d" % (x, total))
    if total < 200:
        print ("%s failed" % x)
    else:
        print ("%s passed)" % y)
