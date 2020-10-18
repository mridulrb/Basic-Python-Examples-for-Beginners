n=input("Enter no of records:")
s=[]
for i in range(n):
    studentno=input("Enter Student no.:")
    studentname=raw_input("Enter Student name:")
    mk1=input("Enter marks:")
    mk2=input("Enter marks:")
    mk3=input("Enter marks:")
    mk4=input("Enter marks:")
    mk5=input("Enter marks:")
    t=mk1+mk2+mk3+mk4+mk5
    avg=t/5
    s+=[[studentno,studentname,mk1,mk2,mk3,mk4,mk5,t,avg]]
for i in range(len(s)):
    for j in range(len(s[i])):
        print s[i][j],
    print
a=0
for i in range(len(s)):
    if(s[i][2]>a):
        a=s[i][2]
        j=i
b=0
print "Topper in Subject 1",s[j]
for i in range(len(s)):
    if(s[i][3]>b):
        c=s[i][3]
        j=i
print "Topper in Subject 2",s[j]
c=0
for i in range(len(s)):
    if(s[i][4]>c):
        c=s[i][4]
        j=i
print "Topper in Subject 3",s[j]
d=0
for i in range(len(s)):
    if(s[i][5]>d):
        d=s[i][5]
        j=i
print "Topper in Subject 4",s[j]
for i in range(len(s)):
    if(s[i][6]>a):
        a=s[i][6]
        j=i
print "Topper in Subject 5",s[j]
a=s[0][2]
for i in range(len(s)):
    if(s[i][2]<a):
        a=s[i][2]
        j=i
print "Failure in Subject 1",s[j]
a=s[0][3]
for i in range(len(s)):
    if(s[i][3]<a):
        a=s[i][3]
        j=i
print "Failure in Subject 2",s[j]
a=s[0][4]
for i in range(len(s)):
    if(s[i][4]<a):
        a=s[i][4]
        j=i
print "Failure in Subject 3",s[j]
a=s[0][5]
for i in range(len(s)):
    if(s[i][5]<a):
        a=s[i][5]
        j=i
print "Failure in Subject 4",s[j]
a=s[0][6]
for i in range(len(s)):
    if(s[i][6]<a):
        a=s[i][6]
        j=i
print "Failure in Subject 5",s[j]
t1=0
for i in range(len(s)):
    if(s[i][7]>t1):
        t1=s[i][7]
        j=i
print "First Topper:",s[j]
s[j]
t2=0
for i in range(len(s)):
    if(s[i][7]>t2 and s[i][7]<t1):
        t2=s[i][7]
        j=i
print "Second Topper:",s[j]
t3=0
for i in range(len(s)):
    if(s[i][7]>t3 and s[i][7]<t3):
        t3=s[i][7]
        j=i
print "Third Topper:",s[j]




    
