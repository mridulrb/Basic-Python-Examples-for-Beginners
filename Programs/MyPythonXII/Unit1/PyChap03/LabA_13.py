# File name: ...\\MyPythonXII\Unit1\PyChap03\LabA_13.py
# Program to calculate general tax
Emp = []
ctr = 1
# Entering 20 employees information
while ctr <= 3 :
    print()
    PNo = input("Enter PAN number: ")
    Name = input("Enter Name: ")
    ASalary = float(input("Enter taxable income: "))
    Temp = (PNo, Name, ASalary) # Creating a tuple
    Emp.append(Temp) # A tuple added into a list
    ctr += 1

# Function to calculate annual tax
def taxcalculator(anSal):
    if (anSal > 200000):
        if ((anSal >= 200000) and (anSal < 500000)):
            tax = (anSal - 200000) * 10/100
        elif ((anSal >= 500000) and (anSal < 1000000)):
            tax = 30000 + (anSal - 500000) * 20/100
        elif (anSal >= 1000000):
            tax = 130000 + (anSal - 1000000) * 30/100
        AnnualTax = tax
    else:
        AnnualTax = 0
    return AnnualTax

# Displaying data in tabular form
print()
print ("Employee tax calculation....")
print()
print ("{0:12} {1:25} {2:>15} {3:>15}".format("PAN No.", "Name", "Annual Salary", "Tax"))
print ("-" * 70)
for Temp in Emp:
    PNo, Name, ASalary = Temp
    Tax = taxcalculator(ASalary)
    print ("{0:12} {1:25} {2:15.2f} {3:15.2f}".format(PNo, Name, ASalary, Tax))
print ("-" * 70)
