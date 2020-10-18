# File name: ...\\MyPythonXII\Unit1\PyChap02\lngrank.py
# File Name : Assign41.py
# Program to print a language table with its international market rating
Language = list()
Ch = 'Y'
while (Ch == 'Y' or Ch == 'y'):
    print()
    Lname = input("Enter language name: ")
    YearD = int(input("Enter year of development: "))
    Rating = float(input("Enter rating: "))
    Lang = (Rating, YearD, Lname) # Creating a tuple
    Language.append(Lang) # A tuple added into a list
    print("Do you want to enter more language <y/n>: ", end="")
    Ch = input()
    if Ch == 'n' or Ch == "N" or Ch == "No":
        break
    
# Displaying data in tabular form
Language.sort(reverse=True)
print()
print ("Computer Languages with International Rating")
print ("="*46)
print ("{0:<12} {1:^16} {2:>16}".format("Language", "Year Developed", "Market rating"))
print ("-"*46)
for element in Language:
    print ("{0:12} {1:^16} {2:16.2f}".format(element[2], element[1], element[0]))
print ("-"*46)
                
