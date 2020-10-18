# File name: ...\\MyPythonXII\Unit1\PyChap02\LabA_07.py
# Program to check if it is a leap year or not
# Note. A year is a leap year if it is divisible by 4, but century years are not
# leap years unless they are divisible by 400.
# Checking input year is valid or not
validYear = False
while not validYear:
    String = input("Enter a year (e.g. 2004): ")
    i = 0
    validYear = True
    while i < len(String):
        if not (String[i] >= '0' and String[i] <= '9') :
            validYear = False
            print ('You entered an invalid year. Please try again')
            break
        i=i+1
    if len(String) != 4:
        print("Year must be a 4 digit number")
        validYear = False
year = int(String)
Flag = 0
if ((year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))):    
    print("The year %d is a leap year." %year)
    Flag = 1
else:
    print("The year %d is a not leap year." %year)
Months = [('January', 31), ('February', 28), ('March', 31), ('April', 30), ('May', 31), ('June', 30),
          ('July', 31), ('August', 31), ('September', 30), ('October', 31), ('November', 30), ('December', 31)]
print()
print("Calender year : %d" %year)
print("====================")
print ("{0:<12} {1:<15} {2:>10}".format("Month No.", "Month Name", "Days"))
print ("-" * 40)
Ctr = 1
for MItem in Months:
    Month, Days = MItem
    if Flag == 1 and Month == "February":
        Days += 1
    print ("{0:<12} {1:<15} {2:>10}".format(Ctr, Month, Days))
    Ctr += 1
print ("-" * 40)
