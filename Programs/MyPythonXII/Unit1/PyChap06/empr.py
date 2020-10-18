# File name: ...\\MyPythonXII\Unit1\PyChap06\empr.py
# Program to read and write employee data
import os
EFile = 'Emp.DAT'
# Function to append employee record
def writeEmployee(EFile):
    Eobj = open(EFile, 'a')
    if not Eobj:
        print ("File does not created")
    else:
        print("Enter employee data")
        ch = 'Y'
        while ch=='Y' or ch=='y':
            ecode = int(input("Enter code: "))            
            name = input("Enter name: ")
            salary = float(input("Enter salary: "))
            # Concatenate data to write in one line
            Eobj.write(str(ecode) + "-" + name.upper() + "-" + str(salary) + "\n")
            ch = input("Add more entry? <y/n>: ")
            if ch == 'y' or ch == 'Y':
                continue
            else:        
                break
    Eobj.close()
    
# Function to read employee records
def readEmployee(EFile):
    Eobj = open(EFile, 'r')
    if not Eobj:
        print ("File does not created")
    else:
        print ("Employees whose salary between - 40,000 and 60,000")
        print ("=" * 50)
        print ("{0:^10} {1:20} {2:^12}".format("Code", "Name", "Slary"))
        print ("-" * 50)
        for emp in Eobj:
            # Strip off the new-line character and any whitespace on the right.
            record = emp.rstrip()
            # Returns a list of all the words in the string using '-' separator
            nemp = record.split('-')
            listLen = len(nemp)
            ecode = int(nemp[0]) # Employee code
            name = nemp[1]  # Employee name
            salary = float(nemp[2]) # Employee salary
            if salary >= 40000 and salary <= 60000:
                print ("{0:^10} {1:20} {2:>10}".format(ecode, name.lstrip(' '), salary))
        print ("-" * 50)
    Eobj.close()

def main():
    opt = 0
    while True:
        print()
        print ("Employee Record")
        print ("-" * 20)
        print()
        print ("1. Employee entry")
        print ("2. Employee display")
        print ("3. Exit")
        print ("Enter your choice: ", end="")
        opt = int(input())
        if opt == 1:
            writeEmployee(EFile)
        elif opt == 2:
            print()
            readEmployee(EFile)
        elif opt == 3:
            break
if __name__ == "__main__":
    main()
