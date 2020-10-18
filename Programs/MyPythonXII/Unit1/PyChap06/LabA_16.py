# File name: ...\\MyPythonXII\Unit1\PyChap06\sdata.py
# Class XII student record management
import os
File = 'Class12.dat'
# Function to perform read/display data
def read_from_file(File):
    if os.path.isfile(File):
        Student = []    # To store all the records in a nested list/matrix
        fobj = open(File)
        std = [] # To store single record in a list
        ctr = -1
        while True:     # To read linewise data from data file
            ctr += 1
            F = fobj.readline()
            if len(F) <= 0:
                break; # Encounter EOF
            # Terminating new line from readline data
            F = F.rstrip('\n')
            F = F.lstrip('\n')
            if ctr <= 6:    # checks if 7 rows are read or not from data file
                            # because each 7 row is a student record
                if F.isdigit():  # Checks if the string contains only digits or not
                    F = int(F)  # Converts string into integer
                    std.append(F) # Append a field into a list
                else:
                    std.append(F) # Appends a string 
            else:
                # When 7 rows, i.e., one records completed, it add into nested list 
                Student.append(std) 
                ctr = 0 # Control reassign 0 for next 7 data field
                std = [] # List for next record
                std.append(F) # appending next record's first field
        Student.append(std) # For appending last record
        # Steps to display records in tabular form
        print()
        print (" " * 40, "Student Marksheet")
        print (" " * 40, "=" * 17)
        print ("{0:8} {1:16} {2:^8} {3:^8} {4:^10} {5:^7} {6:^7} {7:^7} {8:^10} {9:^7}"
               .format("Roll No.", "Name", "English", "Physics", "Chemistry",
                       "Maths", "Computer", "Total", "Percentage", "Grade"))
        # Processing the Student matrix to calculate total, percentage and garde
        print ("-" * 100)
        for i in range(len(Student)): # len(Student) is the total number of rows in matrix
            k = 0
            std = []
            for j in range(7): # j is the total number of columns, i.e., 7
                std.append(Student[i][k]) # First row data appended into a list (std)
                k+=1
            # Last 5 elements in the list (std) are the marks
            Total = std[2] + std[3] + std[4] + std[5] + std[6]
            Per = Total / 5
            # if name is ‘xxx...’ then assume as space(s).
            if std[1] == 'xxxxxxxxxxx':
                std[1] = " "
            # Calling function for grade
            Grade = calGrade(Per)
            print("{0:^8}{1:16}{2:^8}{3:^8}{4:^10}{5:^7}{6:^7}{7:^7}{8:^10}{9:^7}"
                   .format(std[0], std[1], std[2], std[3], std[4], std[5],
                           std[6], Total, Per, Grade))
        print ("-" * 100)
        fobj.close()

# Function to calculate Grade
def calGrade(Per):
    # Grade calculation condition
    if Per >= 90:
        Grade = 'A+'
    elif Per >= 80 and Per < 90:
        Grade = 'A'
    elif Per >= 70 and Per < 80:
        Grade = 'B'
    elif Per >= 60 and Per < 70:
        Grade = 'C'
    elif Per >= 50 and Per < 60:
        Grade = 'D'
    elif Per >= 40 and Per < 50:
        Grade = 'E'
    elif Per < 40:
        Grade = 'F'
    return Grade
# Function to perform write data into data file
def write_to_file(Rollno, Name, EngM, PhyM, ChemM, MathM, CompM):
    fobj = open(File, 'a')
    if not fobj:
        print ("File does not created")
    else:
        # Data is written in form of strings
        fobj.write(str(Rollno)+'\n')
        fobj.write(Name+'\n')
        fobj.write(str(EngM)+'\n')
        fobj.write(str(PhyM)+'\n')
        fobj.write(str(ChemM)+'\n')
        fobj.write(str(MathM)+'\n')
        fobj.write(str(CompM)+'\n')
        fobj.close()

def main():
    choice = 0
    while True:
        print()
        print (" " * 20, "Class XII Student Record")
        print (" " * 20, "-" * 26)
        print()
        print (" " * 20, "1. Student entry")
        print (" " * 20, "2. Student display")
        print (" " * 20, "3. Exit")
        print (" " * 20, "Enter your choice: ", end="")
        choice = int(input())
    
        if choice == 1:
            print()
            ch = 'Y'
            while ch=='Y' or ch=='y':
                # Validation checking for roll no.
                while True:
                    print ("Enter roll no.: ", end="")
                    Rollno = input()
                    rlen = len(Rollno)
                    i = 0
                    Flag = 0
                    while i < rlen:
                        if (Rollno[i] > '0') and (Rollno[i] < '9'):
                            Flag = 1
                            i += 1
                        else:
                            Flag = 0
                            break
                    if Flag == 1:
                        break
                    else:
                        print ("Enter valid roll no.")
                        continue
                Rollno = int(Rollno) # Converts string to int
                print ("Enter name: ", end="")
                Name = input()
                if len(Name) == 0:
                    Name = 'xxxxxxxxxxx'
                print ("Enter English mark: ", end="")
                EngM = int(input())
                print ("Enter Physics mark: ", end="")
                PhyM = int(input())
                print ("Enter Chemistry mark: ", end="")
                ChemM = int(input())
                print ("Enter Mathematics mark: ", end="")
                MathM = int(input())
                print ("Enter Computer mark: ", end="")
                CompM = int(input())
                # Function calling to write into data file
                write_to_file(Rollno, Name, EngM, PhyM, ChemM, MathM, CompM)
                ch = input("Do you want add more data? <y/n>: ")
                if ch=='y' or ch=='Y':
                    continue
                else:
                    break
        elif choice == 2:
            print()
            read_from_file(File)
        elif choice == 3:
            break
if __name__ == "__main__":
    main()
