# File name: ...\\MyPythonXII\Unit1\PyChap06\stwline.py
import os
filename = "Nstd.txt"
def file_write(filename):
    fileobj = open(filename, 'a')
    if not fileobj:
        print ("File does not created")
    else:
        Student = [] # A list to store student data
        ch ='Y'
        print("Enter student information")
        while ch=='Y' or ch=='y':
            print()
            RNo = int(input("Enter roll no.: "))
            # Converts int to str ending with a comma
            # Appends RNo into Student
            Student.append(str(RNo)+', ') 
            Name = input("Enter Name: ")
            Name = Name.upper()
            # Appends Name into Student ending with a comma
            Student.append(Name + ', ')
            Marks = float(input("Enter total marks: "))
            # Converts float to str ending with a comma
            # Appends Marks into Student
            Student.append(str(Marks)+'\n')
            ch = input("Do you want more entry? <y/n>: ")
            if ch=='y' or ch=='Y':
                continue
            else:
                # Write list of strings Student into file
                fileobj.writelines(Student)
    fileobj.close()
    
def file_read(filename):
    if os.path.isfile(filename):
        fileobj = open(filename, 'r')
        print ("Student information")
        print ("-------------------")
        for line in fileobj.readlines(): # Reads all lines
            print (line, end="")
        fileobj.close()
    else:
        print ("File does not exist.")
def main():
    ch = 0
    while ch != 3:
        print()
        print("Student Menu")
        print("=" * 30)
        print("1. Record Addition")
        print("2. Display Record")
        print("3. Quit")
        print("=" * 30)
        print("Enter your choice: ", end="")
        ch = int(input())
        if ch == 1:
            file_write(filename)
        elif ch == 2:
            file_read(filename)
        elif ch == 3:
            break
        
if __name__ == "__main__":
    main()


