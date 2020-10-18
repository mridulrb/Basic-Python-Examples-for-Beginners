class Teacher:
    TNo = Tname = Dept = ' '
    Workload = 0
    Salary = 0
    def TEntry(self):
        print ("Enter teacher data")
    def TDisplay(self):
        print ("Print teacher data")
class Student:
    Admno = SName = Stream = ' '
    Attendance = TotMarks = 0
    def SEntry(self):
        print ("Enter student data")
    def SDisplay(self):
        print ("Print student data")
class School(Student, Teacher):
    SCode = SchName = ' '
    def __init__(self):
        self.SCode = ' '
        self.SchName = ' '
    def SchEntry(self):
        print ("Enter school data")
    def SchDisplay(self):
        print ("Print school data")
