# File name: ...\\MyPythonXII\Unit1\PyChap02\wagecal.py
# Calculating the total wage

def main():
    TotalHours = float(input('Enter hours worked: '))
    HourlyWage = float(input('Enter the wage paid per hour: '))
    if TotalHours <= 40:
        RegularHours = TotalHours
        OverTime = 0
    else:
        OverTime = TotalHours - 40
        RegularHours = 40

    TotalWage = HourlyWage * RegularHours + (0.35 * HourlyWage) * OverTime
    print('Total weekly wage is: %0.2f.' % TotalWage)
main()
