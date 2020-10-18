# File name: ...\\MyPythonXII\Unit1\PyChap06\fsearch.py
import os
File1 = "Flight.TXT"
# Function to search and display details of all flights
def searchFlight():
    if os.path.isfile(File1):
        flobj = open(File1, 'r')
        for f in flobj:
            # Strip off the new-line character and any whitespace on the right.
            flight = f.rstrip()
            flight = flight.upper() 
            FList = flight.split('-')
            if FList[1] == 'MUMBAI':
                print(FList[0], "    ", FList[1], "    ", FList[2])
        flobj.close()
    else:
        print ("Source file does not exist.")

# Function calling
searchFlight()
#Note. See flwrite.py for flight data entry
