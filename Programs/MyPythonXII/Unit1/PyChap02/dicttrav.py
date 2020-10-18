# File name: ...\\MyPythonXII\Unit1\PyChap02\dicttrav.py
# Traversing a dictionary
Student = { "Name" : "Surbhi Gupta",
            "Rollno" : "11",
            "Address" : "F2/27 - MIG Flat, Sec-7, Rohini",
            "Phone" : "7286798500" }
# Traversing dictionary with loop
for key, value in Student.items():
    print (key, "is:", value)
