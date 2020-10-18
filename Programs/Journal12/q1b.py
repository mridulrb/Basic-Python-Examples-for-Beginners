FLIGHT={}
d={}
n=input("Enter no of records:")
for i in range(n):
    flno=raw_input("Enter Flight no.:")
    flname=raw_input("Enter Flight name:")
    dest=raw_input("Enter Flight Destination:")
    d['Flight_Name']=flname
    d['Destination']=dest
    FLIGHT[flno]=d
    d={}
l=[]
for j in FLIGHT:
    if(FLIGHT[j]['Destination']=="Mumbai"):
        l=[[j,FLIGHT[j]]]
print l
flname=[]
for k in FLIGHT:
    flname=flname+[FLIGHT[k]['Flight_Name']]
flname.sort()
print flname
    
