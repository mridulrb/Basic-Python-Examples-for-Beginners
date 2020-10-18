# File name: ...\\MyPythonXII\Unit1\PyChap06\stmenu.py
import os
filename = "Student.txt" 
def student_entry(filename):
    fileobj = open(filename, 'a')
    if not fileobj:
        print ("File does not created")
    else:
        ch ='Y'
        print("Enter student information")
        while ch=='Y' or ch=='y':
            rollno = input("Enter roll no.: ")
            name = input("Enter name: ")
            address = input("Enter address: ")
            # Write record using a comma separator after first field rollno
            fileobj.write(str(rollno) + ", " + name.upper() + " - " + address + "\n")
            ch = input("Do you want more entry? <y/n>: ")
            if ch=='y' or ch=='Y':
                continue
            else:
                break
    fileobj.close()
def student_read(filename):
    if os.path.isfile(filename):
        fileobj = open(filename)
        print ("Student information")
        print ("-------------------")
        for Student in fileobj: # Process till EOF
            print (Student, end="")
        fileobj.close()
    else:
        print ("File does not exist.")
def student_search(filename):
    if os.path.isfile(filename):
        fileobj = open(filename)
        rollno = int(input("Enter roll no. to search: "))
        flag = False # To check if record not found
        for Student in fileobj:
            Strlen = len(Student)
            i = 0
            StrRollno = ""
            while True:
                if Student[i] == ',': # loop will break after finding first comma.
                    break
                # Extracting numbers from Student for rollno.
                if Student[i] >= '0' and Student[i] <= '9':
                    StrRollno = StrRollno + Student[i]
                    i += 1
            Nrollno = int(StrRollno) # Str object converted into integer type
            # Checks if the entered roll number match with file data
            if rollno == Nrollno: 
                print ("Student found: ", Student, end="")
                flag = True
                break
        fileobj.close()
        if flag == False:
            print ("Record does not found.")
    else:
        print ("File does not exist.")    

def getChoice(menu):
    print (menu)
    choice = int(input("Select a choice(1-4): "))
    return choice

def main():
    theMenu = '''
    Student Menu
    - - - - - - - -
    1) Add new student
    2) Display student details
    3) Search student
    4) Quit and save
    '''
    choice = getChoice(theMenu)
    while choice != 4:
        if choice == 1:
            student_entry(filename)
        elif choice == 2:
            student_read(filename)
        elif choice == 3:
            student_search(filename)
        else: print ("Invalid choice, try again")
        choice = getChoice(theMenu)
if __name__ == "__main__":
    main()

