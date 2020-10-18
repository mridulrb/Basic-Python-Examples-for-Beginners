STUDENT={}
n=input("Enter no of records:")
for i in range(n):
    d={}
    name=raw_input("Enter name:")
    marks=[]
    for j in range(5):
        mark=input("Enter marks:")
        marks=marks+[mark]
    d['stream']=raw_input("Enter stream:")
    d['marks']=marks
    STUDENT[name]=d
for j in STUDENT:
    marks=STUDENT[j]['marks']
    marksum=0
    for k in marks:
        marksum=marksum+k
    print "Name:",j,",Stream:",STUDENT[j]['stream'],",Total Marks:",marksum,",Average Marks:",marksum/5
