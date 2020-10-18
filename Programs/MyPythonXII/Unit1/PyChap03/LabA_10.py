# File name: ...\\MyPythonXII\Unit1\PyChap03\LabA_l0.py
# Program to find capital and population for a country
Country = []
Ch = 'Y'
while (Ch == 'Y' or Ch == 'y'):
    print()
    Cname = input("Enter country name.: ")
    Capital = input("Enter capital name: ")
    Population = int(input("Enter population: "))
    C = (Population, Cname, Capital) # Creating a tuple
    Country.append(C) # A tuple added into a list
    print("Do you want to enter more country <y/n>: ", end="")
    Ch = input()
    if Ch == 'n' or Ch == "N" or Ch == "No":
        break
    
# Search a country with respective capital and population
Cnm = input("Enter the country name which you want: ")
CapName = " "
Popl = 0
Flag = 0
for C in Country:
    Population, Cname, Capital = C
    if (Cnm == Cname):
        CapName = Capital
        Popl = Population
        Flag = 1
        break

# Displaying data in tabular form
Country.sort(reverse=True)
print()
print ("Country List....")
print ("-" * 56)
print ("{0:15} {1:15} {2:15}".format("Country", "Capital", "Population"))
print ("-" * 56)
for C in Country:
    Population, Cname, Capital = C
    print ("{0:15} {1:15} {2:15}".format(Cname, Capital, Population))    
print ("-" * 56)
if Flag == 1:
    print("Search country:", Cnm)
    print("Capital:", CapName)
    print("Population", Popl)
else:
      print("Search country %s does not found in list" %Cnm)
    
