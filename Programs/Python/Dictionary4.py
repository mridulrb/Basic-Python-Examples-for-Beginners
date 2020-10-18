matches={}
matches1={}
games=[]
n=input("Enter no of teams")
for i in range(n):
    teamname=raw_input("Enter team name")
    wins=raw_input("Enter no of games won")
    losses=raw_input("Enter no of games lost")
    games=[wins,losses]
    matches[teamname]=games
    matches1[teamname]={'wins':wins,'losses':losses}
print matches
while 1:
    print "Select an option"
    print "1)Winning Percentage"
    print "2)No of wins"
    print "3)Winning Record"
    print "4)Exit"
    option=int(raw_input("Enter option"))
    if(option==1):
        teamname=raw_input("Enter Team name")
        a=float(matches1[teamname]['wins'])
        b=float(matches1[teamname]['losses'])
        percentage=(a/(a+b))*100
        print percentage
    elif(option==2):
        for i in matches1:
            print matches1[i]['wins']
    elif(option==3):
        record=[]
        for i in matches1:
            if(int(matches1[i]['wins'])>20):
                record=record+[i]
            print record
    elif(option==4):
        break
                
