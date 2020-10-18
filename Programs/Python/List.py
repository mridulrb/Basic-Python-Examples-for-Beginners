n=input("Enter no of employees:")
a=[]
b=[]
c=[]
max=0
for i in range(n):
    name=raw_input("Enter name:")
    desig=raw_input("Enter designation:")
    salary=input("Enter salary:")
    b=b+[name]+[desig]+[salary]
    a=a+[b]
    b=[]
for l in range(len(a)):
    print a[l]
for j in range(len(a)):
    if(a[j][2]>max):
        max=a[j][2]
        c=a[j]
    else:
        continue
print "Highest Paid Employee",c
    
