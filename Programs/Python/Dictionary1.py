employees={}
n=input("Enter no of employees")
for i in range(n):
    name=raw_input("Enter employees name")
    salary=input("Enter salary")
    employees[name]=salary
print employees
for j in employees:
    if(employees[j]>10000):
        print j,employees[j],"manager"
    elif(employees[j]<5000):
        print j,employees[j],"not eligible"
