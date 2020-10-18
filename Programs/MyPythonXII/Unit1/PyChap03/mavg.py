# File name: ...\\MyPythonXII\Unit1\PyChap03\mavg.py
# Average marks of 10 students
Marks = [ ]	# An empty list
print ("Enter 10 students total marks.")
for i in range (10) :
    print("Enter marks for student %d: " % int(i+1), end="")
    m = int(input())
    Marks.append(m)
Total = Avg = 0
for i in range(10):
    Total = Total + Marks[i]
Avg = Total / 10
print ("Average marks is: %0.2f" %Avg)
