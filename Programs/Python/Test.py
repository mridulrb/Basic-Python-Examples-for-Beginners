student={}
n=input("Enter range:")
for i in range(n):
    a={}
    name=raw_input("Enter name:")
    stream=raw_input("Enter stream:")
    b=[]
    for j in range(3):
        marks=input("Enter marks:")
        b=b+[marks]
    a[stream]=b
    student[name]=a
print student
for k in student:
    a=student[k]
    for l in a:
        m=a[l]
        s=0
        for n in m:
            s=s+n
        print k,student[k],"Sum:",s,"Average:",s/3
        
