# File name: ...\\MyPythonXII\Unit1\PyChap02\LabA_09.py

# Function to calculate grade
def Cal_Grade(Per):
    Grd = " "
    if Per > 91 :
        Grd = "A1"
    elif Per > 81 and Per <= 90:
        Grd = "A2"
    elif Per > 71 and Per <= 80:
        Grd = "B1"
    elif Per > 61 and Per <= 70:
        Grd = "B2"
    elif Per > 51 and Per <= 60:
        Grd = "C1"
    elif Per > 41 and Per <= 50:
        Grd = "C2"
    elif Per > 33 and Per <= 40:
        Grd = "D"

# Calculating total, percentage and grade 
Student = []
ctr = 1
# Entering 40 best students information
while ctr <= 40 :
    print()
    Name = input("Enter Name: ")
    Name = Name.upper()
    Sub1 = float(input("Enter first subject marks: "))
    Sub2 = float(input("Enter second subject marks: "))
    Sub3 = float(input("Enter third subject marks: "))
    Sub4 = float(input("Enter fourth subject marks: "))
    Sub5 = float(input("Enter fifth subject marks: "))
    Std = (Name, Sub1, Sub2, Sub3, Sub4, Sub5) # Creating a tuple
    Student.append(Std) # A tuple added into a list
    ctr += 1

print()
print ("Student list....")
print()
print ("-" * 110)
print ("{0:<13} {1:>12} {2:>12} {3:>12} {4:>12} {5:>12} {6:>8} {7:>12} {8:^10}"
       .format("Name", "Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5",
               "Total", "Percentage", "Grade"))
print ("-" * 110)
for Std in Student:
    Total = Per = 0
    Grade = " "
    Name, Sub1, Sub2, Sub3, Sub4, Sub5 = Std
    Total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
    Per = Total / 5
    Grade = Cal_Grade(Per)
    print ("{0:<13} {1:>12} {2:>12} {3:>12} {4:>12} {5:>12} {6:>8} {7:>12.2f} {8:^10}"
       .format(Name, Sub1, Sub2, Sub3, Sub4, Sub5, Total, Per, Grade))

print ("-" * 110)

    
