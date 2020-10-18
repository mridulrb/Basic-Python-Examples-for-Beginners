a=[6,5,4,3,2,1]
asc=0
dsc=0
for i in range(len(a)-1):
    if(a[i]>a[i+1]):
        dsc+=1
    elif(a[i]<a[i+1]):
        asc+=1
if(asc==(len(a)-1)):
    print "Ascending"
elif(dsc==(len(a)-1)):
    print "Descending"
elif(asc!=(len(a)-1) or dsc!=(len(a)-1)):
    print "Not sorted"
