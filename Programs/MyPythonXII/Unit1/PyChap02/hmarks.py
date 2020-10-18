# File name: ...\\MyPythonXII\Unit1\PyChap02\hmarks.py
# Program to find highest marks
Students = []
ctr = 1
while ctr <= 5:
    print ("For student: ", ctr, end="")
    print()
    Sname = input("Enter name: ")
    Marks = int(input("Enter marks: "))
    std = (Marks, Sname)
    Students.append(std)
    ctr+=1
    
Students.sort(reverse=True) # sorting according to marks
hmarks = Students[0][0]
name = Students[0][1]
if len(Students) > 0:
    print ("Student Name\t\tMarks")
    print ("------------\t\t------")
    for std in Students:
        Marks, Sname = std
        print (Sname, "\t\t", Marks)
else:
    print ("The list is empty")
    
print ("Highest marks %d is obtained by %s." % (hmarks, name))
        
    
