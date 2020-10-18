# File name: ...\\MyPythonXII\Unit1\PyChap06\teler.py
# Program to read and write telephone data
import os
File = 'Tele.DAT'
# Function to append customer record
def customerAppend(File):
    fobj = open(File, 'a')
    if not fobj:
        print ("File does not created")
    else:
        print("Enter customer data")
        ch = 'Y'
        while ch=='Y' or ch=='y':
            name = input("Enter name: ")
            Teleno = input("Enter telephone no.: ")
            # Concatenate data to write in one line
            fobj.write(str(Teleno) + ", " + name.upper() + "\n")
            ch = input("Add more entry? <y/n>: ")
            if ch == 'y' or ch == 'Y':
                continue
            else:        
                break
    fobj.close()
# Function to search customer record
def customerRead(File, Teleno):
    fobj = open(File, 'r')
    for cust in fobj:
        # Strip off the new-line character and any whitespace on the right.
        record = cust.rstrip()
        NTeleno = ""
        Flag = i = 0
        while True:
            if record[i] == ',': # loop will break after finding first comma.
                break
            # Extracting Telephone no.
            if record[i] >= '0' and record[i] <= '9':
                NTeleno = NTeleno + record[i]
                i += 1
        if Teleno == NTeleno:
            print ("Cusomer details is: ", record)
            Flag = 1
            break
    if Flag == 0:
        print ("Record not found")
    fobj.close()

def main():
    opt = 0
    while True:
        print()
        print ("Telephone Customer")
        print ("-" * 20)
        print()
        print ("1. Cusomer entry")
        print ("2. Customer display")
        print ("3. Exit")
        print ("Enter your choice: ", end="")
        opt = int(input())
        if opt == 1:
            customerAppend(File)
        elif opt == 2:
            print()
            Teleno = input("Enter telephone no. to search: ")
            customerRead(File, Teleno)
        elif opt == 3:
            break
if __name__ == "__main__":
    main()
