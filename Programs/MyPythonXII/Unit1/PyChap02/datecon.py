# File name: ...\\MyPythonXII\Unit1\PyChap02\datecon.py
# Date converter
def main():
    # Enter the date
    dateStr = input("Enter a date (mm/dd/yyyy): ")
    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # Convert monthStr to the month name
    months = ["January", "February", "March", "April", 
              "May", "June", "July", "August", 
              "September", "October", "November", "December"]
    monthStr = months[int(monthStr)-1]

    # Output result in month day, year format
    print("The converted date is:", monthStr, dayStr+",", yearStr)

main()
