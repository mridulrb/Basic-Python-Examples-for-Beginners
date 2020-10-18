n=input("Enter the number of students")
student={}
for i in range(n):
        name=raw_input("Enter name")
        grno=raw_input("Enter GR No.")
        age=raw_input("Enter age")
        val=grno,age
        d1={}
        mk1=raw_input("Enter marks")
        mk2=raw_input("Enter marks")
        mk3=raw_input("Enter marks")
        mk4=raw_input("Enter marks")
        mk5=raw_input("Enter marks")
        marks=[mk1,mk2,mk3,mk4,mk5]
        d1[val]=marks
        student[name]=val,d1[val]
print student
