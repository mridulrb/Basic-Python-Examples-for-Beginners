student={}
n=input("Enter no of students")
for i in range(n):
    rollno=raw_input("Enter roll no.")
    name=raw_input("Enter name")
    student[rollno]=name
while 1:
    print "Select an option"
    print "1)Add"
    print "2)Modify"
    print "3)Delete"
    print "4)Display"
    print "5)Exit"
    option=int(raw_input("Enter option"))
    if(option==1):
        key=raw_input("Enter roll no")
        value=input("Enter value")
        student[key]=value
    elif(option==2):
        key=raw_input("Enter roll no")
        value=input("Enter student name")
        student[key]=value
    elif(option==3):
        students={}
        exkey=raw_input("Enter roll no")
        for i in student:
            if(i==exkey):
                continue
            students[i]=student[i]
        for j in students:
            print j,students[j]
    elif(option==4):
        for i in student:
            print i,student[i]
    elif(option==5):
        break
        
