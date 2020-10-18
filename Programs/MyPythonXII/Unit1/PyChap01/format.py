# File name: ...\\MyPythonXII\Unit1\PyChap01\format.py
# Using field format character code
RollNo = 100
Name = "Mr. Amit Kumar"
ClSection = "XII-A"
DOB = "29-09-1997"
TotalMarks = 454
Percentage = TotalMarks / 5
print ("Roll No.: %d" % RollNo) # A simple integer format
# 20 character format with right-justified
print ("Name: %:20s" % Name) 
# 15 character format with left-justified 
print ("Class and section: %-15s" % ClSection) 
print ("Date of birth: %15s" % DOB) # 15 character string format
print ("Total marks: %10d" % TotalMarks) # An integer with 10 digit format
# A floating point number with 10 integer and 3 precession format
print ("Percentage: %10.3f" % Percentage) 
