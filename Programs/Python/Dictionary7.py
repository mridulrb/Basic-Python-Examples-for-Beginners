flight={}
d2={}
n=input("Enter no of Flights:")
for i in range (n):
    flname=raw_input("Enter Flight name:")
    d2['Flight_name']=flname
    destination=raw_input("Enter Destination:")
    d2['Destination']=destination
    flno=raw_input("Enter Flight no:")
    flight[flno]=d2
print flight
for j in flight:
    if((flight[j]['Destination'])=='Mumbai'):
        print "Flight no:",j
        print "Flight name:",flight[j]['Flight_name']
        print "Destination:",flight[j]['Destination']
    else:
        continue
