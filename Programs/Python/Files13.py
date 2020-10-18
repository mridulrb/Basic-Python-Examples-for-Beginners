import os
import pickle
x=open("Employee.dat","ab")
n=input("Enter no of employees")
d={}
for i in range(n):
    name=raw_input("Enter name")
    salary=raw_input("Enter salary")
    d[name]=salary
pickle.dump(d,x)
y=open("Employee.dat","rb")
try:
    while True:
        z=pickle.load(y)
        for j in z:
            if(int(d[j])>=5000):
                print z
except EOFError:
    pass
x.close()
y.close()
