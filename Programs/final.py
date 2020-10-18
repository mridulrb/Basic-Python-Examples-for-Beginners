card=["gold","silver","blue","red"]
zone1=["jebel ali","jebel ali industrial"]
zone2=["noor islamic bank","first gulf bank","moe","sharaf dg","dubai internet city","nakheel","dubai marina","jlt","nakheel harbour and tower","ibn battuta","energy"]
zone3=["business bay","dubai mall","difc","emirates towers","dwtc","al jafiliya","al karama","creek","al jadaf","dhc","oud metha","burjuman","al fahidi","al ghubaiba"]
zone4=["al ras","baniyas square","palm deira","union","al rigga","dcc","ggico","terminal 1","terminal 3","emirates","rashidiya","salah al din","abu bakr al siddique","abu hail",
"al qiyadah","stadium","al nahda","dubai airport freezone","al qusais","etisalat"]
print zone1
print zone2
print zone3
print zone4
From=raw_input("FROM  :")
To=raw_input("TO   :")
length=len(card)
length1=len(zone1)
length2=len(zone2)
length3=len(zone3)
length4=len(zone4)
print card
cardtype=raw_input("Choose your Card type :")
if(cardtype=="gold"):
    if (From==To):
        print "Aed.3.6"
    elif ((From in zone1) and (To in zone1)):
        a=zone1.index(From)
        b=zone1.index(To)
        if (b==a+1 or a==b+1):
            print "Aed.3.6"
        else:
            print "Aed.4.6"

    elif ((From in zone2) and (To in zone2)):
        a=zone2.index(From)
        b=zone2.index(To)
        if (b==a+1 or a==b+1):
            print "Aed.3.6"
        else:
            print"Aed.4.6"
    elif ((From in zone3) and (To in zone3)):
        a=zone3.index(From)
        b=zone3.index(To)
        if (b==a+1 or a==b+1):
            print "Aed.3.6"
        else:
            print "Aed.4.6"
        
    elif ((From in zone4) and (To in zone4)):
        a=zone4.index(From)
        b=zone4.index(To)
        if (b==a+1 or a==b+1):
            print "Aed.3.6"
        else:
            print "Aed.4.6"
    
    elif (From!=To):
        for i in range(0,length1):
            a=zone1[i]
            if (a==From):
                r="zone1"
            elif (a==To):
                s="zone1"
        for j in range(0,length2):
           b=zone2[j]
           if (b==From):
                r="zone2"
           elif (b==To):
                s="zone2"
        for k in range(0,length3):
            c=zone3[k]
            if (c==From):
                r="zone3"
            elif(c==To):
                s="zone3"
        for l in range(0,length4):
            d=zone4[l]
            if (d==From):
                r="zone4"
            elif(d==To):
                s="zone4"
        
        
       
            
            
        
        
        if (r=="zone1" and s=="zone2"):
            print "price",":","Aed.8.2"
        elif (r=="zone1" and s=="zone3"):
            print "price",":","Aed.11.6"
        elif (r=="zone1" and s=="zone4"):
            print "price",":","Aed.11.6"
        elif (r=="zone2" and s=="zone1"):
            print "price",":","Aed.8.2"

        elif (r=="zone2" and s=="zone3"):
            print "price",":","Aed.8.2"
        elif (r=="zone2" and s=="zone4"):
            print "price",":","Aed.11.6"
        elif (r=="zone3" and s=="zone1"):
            print "price",":","Aed.11.6"
        elif (r=="zone3" and s=="zone4"):
            print "price",":","Aed.8.2"
            
        elif (r=="zone3" and s=="zone2"):
            print "price",":","Aed.8.2"
        elif (r=="zone4" and s=="zone1"): 
            print "price",":","Aed.11.6"
        elif (r=="zone4" and s=="zone2"):
            print "price",":","Aed.11.6"
        elif (r=="zone4" and s=="zone3"):
            print "price",":","Aed.8.2"
        
if(cardtype=="silver"):
    if (From==To):
        print "Aed.1.8"
    elif ((From in zone1) and (To in zone1)):
     a=zone1.index(From)
     b=zone1.index(To)
     if (b==a+1 or a==b+1):
        print "Aed.1.8"
     else:
        print "Aed.2.3"

    elif ((From in zone2) and (To in zone2)):
        a=zone2.index(From)
        b=zone2.index(To)
        if (b==a+1 or a==b+1):
         print "Aed.1.8"
        else:
         print"Aed.2.3"
    elif ((From in zone3) and (To in zone3)):
     a=zone3.index(From)
     b=zone3.index(To)
     if (b==a+1 or a==b+1):
         print "Aed.1.8"
     else:
         print "Aed.2.3"
        
    elif ((From in zone4) and (To in zone4)):
      a=zone4.index(From)
      b=zone4.index(To)
      if (b==a+1 or a==b+1):
        print "Aed.1.8"
      else:
        print "Aed.2.3"
    
    elif (From!=To):
       for i in range(0,length1):
         a=zone1[i]
         if (a==From):
            r="zone1"
         elif (a==To):
            s="zone1"
       for j in range(0,length2):
         b=zone2[j]
         if (b==From):
              r="zone2"
         elif (b==To):
              s="zone2"
       for k in range(0,length3):
         c=zone3[k]
         if (c==From):
            r="zone3"
         elif(c==To):
            s="zone3"
       for l in range(0,length4):
            d=zone4[l]
            if (d==From):
             r="zone4"
            elif(d==To):
             s="zone4"
        
       
        
       if (r=="zone1" and s=="zone2"):
            print "price",":","Aed.4.1"
       elif (r=="zone1" and s=="zone3"):
            print "price",":","Aed.5.8"
       elif (r=="zone1" and s=="zone4"):
            print "price",":","Aed.5.8"
       elif (r=="zone2" and s=="zone1"):
            print "price",":","Aed.4.1"

       elif (r=="zone2" and s=="zone3"):
            print "price",":","Aed.4.1"
       elif (r=="zone2" and s=="zone4"):
            print "price",":","Aed.5.8"
       elif (r=="zone3" and s=="zone1"):
            print "price",":","Aed.5.8"
       elif (r=="zone3" and s=="zone4"):
            print "price",":","Aed.4.1"
            
       elif (r=="zone3" and s=="zone2"):
            print "price",":","Aed.4.1"
       elif (r=="zone4" and s=="zone1"):
            print "price",":","Aed.5.8"
       elif (r=="zone4" and s=="zone2"):
            print "price",":","Aed.5.8"
       elif (r=="zone4" and s=="zone3"):
            print "price",":","Aed.4.1"
if(cardtype=="blue"):
    if (From==To):
        print "Aed.0.9"
    elif ((From in zone1) and (To in zone1)):
     a=zone1.index(From)
     b=zone1.index(To)
     if (b==a+1 or a==b+1):
        print "Aed.0.9"
     else:
        print "Aed.1.05"

    elif ((From in zone2) and (To in zone2)):
     a=zone2.index(From)
     b=zone2.index(To)
     if (b==a+1 or a==b+1):
        print "Aed.0.9"
     else:
        print"Aed.1.05"
    elif ((From in zone3) and (To in zone3)):
     a=zone3.index(From)
     b=zone3.index(To)
     if (b==a+1 or a==b+1):
        print "Aed.0.9"
     else:
        print "Aed.1.05"
        
    elif ((From in zone4) and (To in zone4)):
     a=zone4.index(From)
     b=zone4.index(To)
     if (b==a+1 or a==b+1):
        print "Aed.0.9"
     else:
        print "Aed.1.05"
    
    elif (From!=To):
     for i in range(0,length1):
      a=zone1[i]
      if (a==From):
        r="zone1"
      elif (a==To):
        s="zone1"
     for j in range(0,length2):
      b=zone2[j]
      if (b==From):
        r="zone2"
      elif (b==To):
        s="zone2"
     for k in range(0,length3):
      c=zone3[k]
      if (c==From):
        r="zone3"
      elif(c==To):
        s="zone3"
     for l in range(0,length4):
      d=zone4[l]
      if (d==From):
        r="zone4"
      elif(d==To):
        s="zone4"
        
      
        
     if (r=="zone1" and s=="zone2"):
            print "price",":","Aed.2.05"
     elif (r=="zone1" and s=="zone3"):
            print "price",":","Aed.2.9"
     elif (r=="zone1" and s=="zone4"):
            print "price",":","Aed.2.9"
     elif (r=="zone2" and s=="zone1"):
            print "price",":","Aed.2.05"

     elif (r=="zone2" and s=="zone3"):
            print "price",":","Aed.2.05"
     elif (r=="zone2" and s=="zone4"):
            print "price",":","Aed.2.9"
     elif (r=="zone3" and s=="zone1"):
            print "price",":","Aed.2.9"
     elif (r=="zone3" and s=="zone4"):
            print "price",":","Aed.2.05"
            
     elif (r=="zone3" and s=="zone2"):
            print "price",":","Aed.2.05"
     elif (r=="zone4" and s=="zone1"):
            print "price",":","Aed.2.9"
     elif (r=="zone4" and s=="zone2"):
            print "price",":","Aed.2.9"
     elif (r=="zone4" and s=="zone3"):
            print "price",":","Aed.2.05"
import datetime
y=datetime.datetime.now()
hour=y.hour
minute=y.minute
if (From=="dhc"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="oud metha"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="jebel ali"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="al qusais"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="etisalat"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="al karama"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="rashidiya"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="burjuman"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="al fahidi"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="al ghubaiba"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand

if (From=="al jadaf"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="creek"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand

if (From=="dubai airport freezone"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="al jafiliya"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="emirates towers"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="dubai mall"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="business bay"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="difc"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="dwtc"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="palm deira"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="business bay"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand

if (From=="terminal 3"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="ggico"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="abu bakr al siddique"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="business bay"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand

if (From=="stadium"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand

if (From=="baniyas square"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand

if (From=="terminal 1"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand


if (From=="emirates"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand



if (From=="salah al din"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand

if (From=="dcc"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand

if (From=="al nahda"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="al qiyadah"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="jebel ali industrial"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand

if (From=="noor islamic bank"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
  
if (From=="dubai internet city"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="dubai marina"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
   
if (From=="nakheel harbour and tower"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",47
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",47
        elif (minute>45):
            print "The next train will arrive at",5,":",55
        elif(minute>53):
            print "The next train will arrive at",6,":",03
    elif(hour==6):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",7,":",07
                break
    elif(hour==7):
        for minhand in range(7,60,8):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",8,":",03
                break
    elif(hour==8):
        for minhand in range(3,60,8):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",9,":",07
                break
    elif(hour==9):
        for minhand in range(7,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",10,":",01
                break
    elif(hour==10):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",11,":",01
                break
    elif(hour==11):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",12,":",01
                break
 
    elif(hour==12):
        for minhand in range(1,60,6):
            if(minhand>=minute and minute<=55):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>55):
                print "The next train will arrive at",13,":",01
                break
    elif(hour==13):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",14,":",05
                break
    elif(hour==14):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",15,":",01
                break
    elif(hour==15):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",16,":",05
                break
    elif(hour==16):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",17,":",05
                break
    elif(hour==17):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",18,":",05
                break
    elif(hour==18):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",19,":",05
                break
    elif(hour==19):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",20,":",05
                break
                
                
    elif(hour==20):
        for minhand in range(5,60,6):
            if(minhand>=minute and minute<=59):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>59):
                print "The next train will arrive at",21,":",05
                break
    elif(hour==21):
        for minhand in range(5,60,8):
            if(minhand>=minute and minute<=53):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>53):
                print "The next train will arrive at",22,":",01
                break
    elif(hour==22):
        for minhand in range(1,60,8):
            if(minhand>=minute and minute<=57):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>57):
                print "The next train will arrive at",23,":",05
                break
    elif(hour==23):
        for minhand in range(5,29,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="first gulf bank"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="energy"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="sharaf dg"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="al rigga"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (From=="nakheel"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
    
if (From=="jlt"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand    
if (From=="ibn battuta"):
    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
        print "The next train will arrive at",5,":",45
    if (hour==5):
        if (minute>44):
            print "The next train will arrive at",5,":",45
        elif (minute>45):
            print "The next train will arrive at",5,":",53
        elif(minute>53):
            print "The next train will arrive at",6,":",01
    elif(hour==6):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",6,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",7,":",06
                break
    elif(hour==7):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",7,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",8,":",02
                break
    elif(hour==8):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",8,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",9,":",06
                break
    elif(hour==9):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",9,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",10,":",02
                break
    elif(hour==10):
        for minhand in range(2,60,6):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",10,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",11,":",04
                break
    elif(hour==11):
        for minhand in range(4,60,6):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",11,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",12,":",06
                break
 
    elif(hour==12):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",12,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",13,":",02
                break
    elif(hour==13):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",13,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",14,":",06
                break
    elif(hour==14):
        for minhand in range(6,60,8):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",14,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",15,":",02
                break
    elif(hour==15):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",15,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",16,":",06
                break
    elif(hour==16):
        for minhand in range(6,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",16,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",17,":",00
                break
    elif(hour==17):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",17,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",18,":",00
                break
    elif(hour==18):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",18,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",19,":",00
                break
    elif(hour==19):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",19,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",20,":",00
                break
                
                
    elif(hour==20):
        for minhand in range(0,60,6):
            if(minhand>=minute and minute<=54):
                print "The next train will arrive at",20,":",minhand
                break
            elif(minute>54):
                print "The next train will arrive at",21,":",00
                break
    elif(hour==21):
        for minhand in range(0,60,8):
            if(minhand>=minute and minute<=56):
                print "The next train will arrive at",21,":",minhand
                break
            elif(minute>56):
                print "The next train will arrive at",22,":",02
                break
    elif(hour==22):
        for minhand in range(2,60,8):
            if(minhand>=minute and minute<=58):
                print "The next train will arrive at",22,":",minhand
                break
            elif(minute>58):
                print "The next train will arrive at",23,":",04
                break
    elif(hour==23):
        for minhand in range(4,26,8):
            if(minhand>=minute):
                print "The next train will arrive at",23,":",minhand
if (To=="dhc"):
    print "The feeder buses available are:"
    print "22-Healthcare city-AL NAHDA 1"
    print "42-GHUBAIBA BUS STATION :AL GHUBAIBA 1"
    print "C7-HOR AL ANZ BUS STATION-HEALTHCARE CITY"
if (To=="rashidiya"):
    print "The feeder buses available are:"
    print "F1- Ras Al Khor"
    print "F2-Mirdif West"
    print "F5-Al Mizhar"
    print "F10-Al Warqa"
    print "365-International City"
if(To=="emirates"):
    print "The feeder buses available are:"
    print "F8-Al Nahda 2"
    print "Mamzar,Century Mall"
if(To=="terminal 3"):
    print "The feeder buses available are:"
    print "C1-Satwa Bus Station"
    print "88-Nakheel MS"
if(To=="terminal 1"):
    print "The feeder buses available are:"
    print "C1-Satwa Bus Station"
    print "4-Gold Souq Bus Station-Rashidiya MS"
    print "11A-Gold souq Bus Station-Al Awir Terminus"
    print "32C-Al Qusais Bus Station-Satwa Bus Station"
    print "33-Ghubaiba Bus Station-Al Qusais Bus Station"
    print "42-Ghubaiba Bus Station-Airport Terminal 1"
    print "48-Mamzar,Century Mall-Rashidiya MS"
    print "64A-Glod Souk Bus Station-Ras Al Khor"
    print "88-Airport Terminal 3-Nakheel MS"
if(To=="ggico"):
    print "The feeder buses available are:"
    print "42-Ghubaiba Bus Station-airport Terminal 1"
if(To=="dcc"):
    print "The feeder buses available are:"
    print "C10-Hamriya Port- Jumeirah Beach Park"
    print "C14-Mamzar,Century Mall-Safa Terminus"
    print "C15-Hamriya Port-Al Wasl Park Terminus"
    print "C19-Ghubaiba Bus Station-Al Qusais Industrial Area"
    print "X28-Lulu Village-Nakheel MS"
    print "22-Health Care City-Al Nahda 1"  
    print "27-Gold Souq Bus Station-Dubai Mall"
    print "33-Ghubaiba Bus Station-Al Qusais Bus Station"
    print "53-Ghubaiba Bus Station-International City"
    print "88-Airport Terminal 3-Nakhell MS"
if(To=="al rigga"):
    print "The feeder buses available are:"
    print "C9-Satwa Bus Station-Hor Al Anz East"
if(To=="union"):
    print "The feeder buses available are:"
    print "C1-Airport Terminal 3-Satwa Bus Station"
    print "C2-Zabeel Park-Airport Terminal 2"
    print "C4-Gold Souq Bus Station-Jadaf"
    print "C5-Gold Souq bus Station-Ghubaiab Bus Satation"
    print "C7-Hor Al Anz Bus Station-Healthcare City"
    print "C9-Satwa Bus Station-Hor Al Anz East "
    print "C28-Gold Souq Bus Station-Mamzar Beach Park"
    print "C55-Gold Souq Bus Station-Ghubaiba Bus Station"
    print "E303-Union Square MS-Sharjah"
    print "E700-Fujairah-Union Square MS"
    print "E400-Union Square MS-Ajman"
    print "X94-Gold Souq Bus Station-Dubai Investment Park"
    print "4-Gold Souq Bus Station-Rashidiya MS"
    print "11A-Gold Souq Bus Station-Al Awir Terminus"
    print "27-Gold Souq Bus Station-Dubai Mall"
    print "64A-Gold Souq Bus Station-Ras Al Khor"
if(To=="burjuman"):
    print "The feeder buses available are:"
    print "C2-Zabeel Park-Airport Terminal 2"
    print "C3-Hor Al Anz Bus Station-Karama Bus Station"
    print "C5-Gold Souq Bus Station-Ghubaiba Bus Station"
    print "C10-Hamriya Port-Jumeirah Beach Park"
    print "C18-Shaikh Rashid Colony,AlQusais-Lamcy Plaza"    
    print "C19-Ghubaiba Bus Station-Al Qusais Industrial Area"
    print "C55-Gold Souq Bus Station-Ghubaiba Bus Station"
    print "X23-Gold Souq Bus Station–International City" 
    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4"
    print "33-Ghubaiba Bus Station–Al Qusais Bus Station" 
    print "42-Ghubaiba Bus Station–Airport Terminal 1"
    print "44-Ghubaiba Bus Station–Dubai Festival City"
    print "61-Ghubaiba Bus Station–Ras Al Khor" 
    print "61D-Ghubaiba Bus Station–Nad Al Sheba Clinic" 
    print "66-Ghubaiba Bus Station–Faqa Terminus"
    print "67-Ghubaiba Bus Station–Endurance City Terminus"
    print "91-Ghubaiba Bus Station–Jebel Ali Bus Station"
if(To=="al karama"):
    print "The feeder buses available are:"
    print "C2-Airport Terminal 2–Zabeel Park"
    print "C10-Hamriya Port–Jumeirah Beach Park"
    print "C15 Hamriya Port–Al Wasl Park"
    print "C26-Al Wasl Park–Al Qusais Industrial Area"
    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4"
    print "61-Ghubaiba Bus Station–Ras Al Khor Industrial Area"
    print "88-Airport Terminal 3–Nakheel MS"
if(To=="al jafiliya"):
    print "The feeder buses available are:"
    print "C2-Zabeel Park–Airport Terminal 2"
    print "C15-Hamriya Port–Al Wasl Park Terminus"
    print "C26-Al Wasl Park Terminus–Al Qusais Industrial Area"
    print "X10-Gold Souq Bus Station–Al Quoz Bus Station" 
    print "X28-Lulu Village–Nakheel MS" 
    print "X92-Ghubaiba Bus Station–Dubai Investment Park"
    print "10-Gold Souq Bus Station–Al Quoz Bus Station" 
    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4" 
    print "27-Gold Souq Bus Station-Dubai Mall" 
    print "61-Ghubaiba Bus Station–Ras Al Khor Ind. Area" 
    print "88-Airport Terminal 3–Nakheel MS"
if(To=="dwtc"):
    print "The feeder buses available are:"
    print "F11-Financial Centre MS–Satwa"
    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4" 
    print "98E-Satwa Bus Station–Al Quoz Ind. Area 3"
if(To=="emirates towers"):
    print "The feeder buses available are:"
    print "F11 Financial Centre MS – Satwa"
    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4"
    print "27-Gold Souq Bus Station–Dubai Mall"
    print "98E-Satwa Bus Station–Al Quoz Ind. Area 3"
if(To=="difc"):
    print "The feeder buses available are:"
    print "F11-Financial Centre MS–Satwa" 
if(To=="dubai mall"):
    print "The feeder buses available are:"
    print "F13-Burj Khalifa/Dubai Mall MS–Dubai Mall"
    print "F16-Burj Khalifa/Dubai Mall MS–Jumeirah 2"
if(To=="business bay"):
    print "The feeder buses available are:"
    print "F16 Dubai Mall – Jumeirah 2" 
    print "F20 Business Bay MS – Al Safa 1"
    print "7-Ghubaiba Bus Station–Iranian Clinic Al Quoz"
if(To=="noor islamic bank"):
    print "The feeder buses available are:"
    print "F15-Noor Islamic Bank MS–Al Quoz Ind. Area 2"
    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4"
if(To=="first gulf bank"):
    print "The feeder buses available are:"
    print "F25-First Gulf Bank MS land side–Al Quoz 3 & 4"
    print "12-Ghubaiba Bus Station–Al Quoz Bus Station"
if(To=="moe"):
    print "The feeder buses available are:"
    print "F30-Mall of the Emirates MS–Arabian Ranches"
    print "F33-Mall of the Emirates MS–Al Barsha 3" 
    print "93-Ghubaiba Bus Station–The Greens"
if(To=="dubai internet city"):
    print "The feeder buses available are:"
    print "F31-The Meadows–Dubai Internet City MS"
    print "88-Airport Terminal 3–Nakheel MS"
    print "X28-Lulu Village–Nakheel MS" 
if(To=="nakheel"):
    print "The feeder buses available are:"
    print "X28-Lulu Village-Nakheel MS"
    print "88-Airport Terminal 3–Nakheel MS"
if(To=="dubai marina"):
    print "The feeder buses available are:"
    print "F37-Marina MS–Dubai Marina"
if(To=="jlt"):
    print "The feeder buses available are:"
    print "F37-Marina MS–Jumeirah Lakes Tower MS–Dubai Marina"
if(To=="ibn battuta"):
    print "The feeder buses available are:"
    print "E101-Abu Dhabi–Ibn Batutta"
    print "F43-Ibn Battuta MS–Discovery Gardens"
    print "F44-Ibn Battuta MS–The Gardens"
    print "F46-Ibn Battuta MS–IMP Zone"
    print "F48-Ibn Battuta MS–Dubai Investment Park"
    print "F53-Ibn Battuta MS–Dubai Industrial City"
    print "8-Ibn Battuta MS–Gold Souk Bus Station"
if(To=="jebel ali"):
    print "The feeder buses available are:"
    print "F54-Jafza South–Jebel Ali MS"
    print "99-New East Camp–Marine Control Towers"
    
if(To=="etisalat"):
    print "The feeder buses available are:"
    print "31-Gold Souq Bus Station–Oud Al Mateena"
if(To=="al qusais"):
    print "The feeder buses available are:"
    print "13 Gold Souq Bus Station – Al Qusais Bus Station"
    print "31-Gold Souq Bus Station–Oud Al Mateena"
    print "64-Gold Souq Bus Station–Ras Al Khor"
if(To=="dubai airport freezone"):
    print "The feeder buses available are:"
    print "13-Gold Souq Bus Station–Al Qusais Bus Station"
    print "17-Al Sabkha Bus Station–Al Qusais Bus Station" 
    print "31-Gold Souq Bus Station–Oud Al Mateena"
    print "64-Gold Souq Bus Station–Ras Al Khor"
    print "C18-Shaikh Rashid Colony, Al Qusais–Lamcy Plaza" 
    print "C19-Ghubaiba Bus Station–Al Qusais Industrial Area"
    print "x28-Lulu Village–Nakheel MS"
if(To=="al nahda"):
    print "The feeder buses available are:"
    print "13 Gold Souq Bus Station–Al Qusais Bus Station"
    print "13A Gold Souq Bus Station–Al Qusais Bus Station"
    print "17 Al Sabkha Bus Station–Al Qusais Bus Station"
    print "22 Healthcare City–Al Nahda 1"
    print "31 Gold Souq Bus Station–Oud Al Mateena"
    print "64 Gold Souq Bus Station–Ras Al Khor"
    print "C18 Shaikh Rashid Colony, Al Qusais–Lamcy Plaza"
    print "C19 Ghubaiba Bus Station–Al Qusais Industrial Area"
    print "X28 Lulu Village–Nakheel MS"
if(To=="stadium"):
    print "The feeder buses available are:"
    print "13-Gold Souq Bus Station–Al Qusais Bus Station"
    print "13A Gold Souq Bus Station–Al Qusais Bus Station"
    print "17 Al Sabkha Bus Station–Al Qusais Bus Station"
    print "22 Healthcare City–Al Nahda 1"
    print "64 Gold Souq Bus Station–Ras Al Khor"
    print "C18 Shaikh Rashid Colony, Al Qusais–Lamcy Plaza"
    print "C19 Ghubaiba Bus Station–Al Qusais Industrial Area"
    print "X28 Lulu Village–Nakheel MS"
if(To=="al qiyadah"):
    print "The feeder buses available are:"
    print "C9-Al Satwa Bus Station–Hor Al Anz East"
if(To=="abu hail"):
    print "The feeder buses available are:"
    print "13 Gold Souq Bus Station–Al Qusais Bus Station"
    print "13A Gold Souq Bus Station–Al Qusais Bus Station"
    print "48 Mamzar, Century Mall–Al Rashidiya MS"
    print "C2 Zabeel Park–Airport Terminal 2"
    print "C3 Hor Al Anz Bus Station–Karama Bus Station"
    print "C7 Hor Al Anz Bus Station–Healthcare City"
    print "C9 Satwa Bus Station–Hor Al Anz East"
    print "C19 Ghubaiba Bus Station–Al Qusais Industrial Area"
    print "X28 Lulu Village–Nakheel MS"
if(To=="abu bakr al siddique"):
    print "The feeder buses available are:"
    print "13 Gold Souq Bus Station–Al Qusais Bus Station"
    print "13A Gold Souq Bus Station–Al Qusais Bus Station"
    print "48 Mamzar, Century Mall–Al Rashidiya MS"
    print "C2 Zabeel Park–Airport Terminal 2"
    print "C19 Ghubaiba Bus Station–Al Qusais Industrial Area" 
    print "x28 Lulu Village–Nakheel MS" 
if(To=="salah al din"):
    print "The feeder buses available are:"
    print "10-Gold Souq Bus Station–Al Quoz Bus Station"
    print "13-Gold Souq Bus Station–Al Qusais Bus Station"
    print "13A-Gold Souq Bus Station–Al Qusais Bus Station"
    print "C2-Zabeel Park–Airport Terminal 2"
    print "C28-Gold Souq Bus Station–Mamzar Beach Park"
if(To=="union"):
    print "The feeder buses available are:"
    print "4-Gold Souq Bus Station–Rashidiya MS"
    print "11A-Gold Souq Bus Station–Al Awir"
    print "27-Gold Souq Bus Station–Dubai Mall"
    print "64A-Gold Souq Bus Station–Ras Al Khor"
    print "C1-Airport Terminal 3–Satwa Bus Station"
    print "C2-Zabeel Park–Airport Terminal 2"
    print "C4-Gold Souq Bus Station–Jadaf"
    print "C5-Gold Souq Bus Station–Ghubaiba Bus Station"
    print "C7-Hor Al Anz Bus Station–Healthcare City"
    print "C9-Satwa Bus Station–Hor Al Anz East"
    print "C28-Gold Souq Bus Station–Mamzar Beach Park"
    print "C55-Gold Souq Bus Station–Ghubaiba Bus Station"
    print "X94-Gold Souq Bus Station–Dubai Investment Park"
if(To=="baniyas square"):
    print "The feeder buses available are:"
    print "17-Al Sabkha Bus Station–Al Qusais Bus Station" 
    print "64A-Gold Souq Bus Station–Ras Al Khor"
if(To=="palm deira"):
    print "The feeder buses available are:"
    print "8-Gold Souq Bus Station–Al Mina Al Siyahi" 
    print "C1-Airport Terminal 3–Satwa Bus Station"
    print "C2-Zabeel Park–Airport Terminal 2" 
    print "C3-Hor Al Anz Bus Station-Karama Bus Station" 
    print "C7-Hor Al Anz Bus Station–Healthcare City"
    print "C9-Satwa Bus Station–Hor Al Anz East"
    print "C18-Shaikh Rashid Colony, Al Qusais–Lamcy Plaza"
    print "C55-Gold Souq Bus Station–Ghubaiba Bus Station"
    print "X10-Gold Souq Bus Station–Al Qouz Bus Station"
    print "X13-LuLu Village–Al Satwa Bus Station"
    print "X23-Gold Souq Bus Station–International City"
if(To=="al ras"):
    print "The feeder buses available are:"
    print "27-Gold Souq Bus Station–Dubai Mall"
    print "53-Ghubaiba Bus Station–International City"
    print "C2-Zabeel Park–Airport Terminal 2"
    print "C4-Gold Souq Bus Station–Jadaf"
    print "C7-Hor Al Anz Bus Station–Healthcare City"
    print "C9-Satwa Bus Station–Hor Al Anz East"
    print "C28-Gold Souq Bus Station–Mamzar Beach Park"
    print "C55-Gold Souq Bus Station–Ghubaiba Bus Station"
if(To=="al ghubaiba"):
    print "The feeder buses available are:"
    print "8-Gold Souq Bus Station–Al Mina Al Siyahi"
    print "C5-Gold Souq Bus Station–Ghubaiba Bus Station"
    print "C7-Hor Al Anz Bus Station–Healthcare City"
    print "C9-Satwa Bus Station–Hor Al Anz East"
    print "X13-LuLu Village–Al Satwa Bus Station"    
if(To=="al fahidi"):
    print "The feeder buses available are:"
    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4"
    print "33-Ghubaiba Bus Station–Qusais Bus Station"
    print "42-Ghubaiba Bus Station–Airport Terminal 1" 
    print "44-Ghubaiba Bus Station–Dubai Festival City" 
    print "61-Ghubaiba Bus Station–Ras Al Khor"
    print "61D-Ghubaiba Bus Station-Nad Al Sheba Clinic"
    print "66-Ghubaiba Bus Station–Faqa Terminus"
    print "67-Ghubaiba Bus Station–Endurance City Terminus"
    print "91-Ghubaiba Bus Station–Jebel Ali Bus Station"
    print "C1-Airport Terminal 3–Satwa Bus Station"
    print "C2-Zabeel Park–Airport Terminal 2"
    print "C3-Hor Al Anz Bus Station–Karama Bus Station"
    print "C5-Gold Souq Bus Station–Ghubaiba Bus Station"
    print "C7-Hor Al Anz Bus Station–Healthcare City"
    print "C18-Shaikh Rashid Colony, Al Qusais–Lamcy Plaza"
    print "C19-Ghubaiba Bus Station-Al Qusais Industrial Area"
    print "C55-Gold Souq Bus Station-Ghubaiba Bus Station"
    print "X23-Gold Souq Bus Station–International City"
if(To=="oud metha"):
    print "The feeder buses available are:"
    print "22-Healthcare City – Al Nahda 1"
    print "42-Ghubaiba Bus Station-Airport Terminal 1"
    print "44-Ghubaiba Bus Station-Dubai Festival City"
    print "61D-Ghubaiba Bus Station-Nad Al Sheba Clinic"
    print "66-Ghubaiba Bus Station-Faqa Terminus"
    print "67-Ghubaiba Bus Station-Endurance City Terminus"
    print "C4-Gold Souq Bus Station-Jadaf"
    print "C7-Hor Al Anz Bus Station-Healthcare City"
    print "C18-Shaikh Rashid Colony, Al Qusais-Lamcy Plaza"
    print "X23-Gold Souq Bus Station–International City"
from math import *
RedLine=["rashidiya","emirates","terminal 3","terminal 1","ggico","dcc","al rigga","union","burjuman","al karama",
"al jafiliya","dwtc","emirates towers","difc","dubai mall","business bay","noor islamic bank",
"first gulf bank","moe","sharaf dg","dubai internet city","nakheel","dubai marina","jlt","nakheel harbour and tower",
"ibn battuta","energy","jebel ali industrial","jebel ali"]
GreenLine=["etisalat","al qusais","airport free zone","al nahda,stadium","al qiyadah","abu bakr al siddique","salah al din","union","baniyas Square",
"palm deira","al ras","al ghubaiba","al fahidi","burjuman","oud metha","dhc","al jadaf","creek"]
Via=["union","burjuman"]

if((From in RedLine) and (To in RedLine) and (From!="burjuman") and (From!="union") and (To!="burjuman") and (To!="union")):
    x=RedLine.index(From)
    y=RedLine.index(To)
    print From,"is",fabs(y-x),"stops from",To
if((From in GreenLine) and (To in GreenLine) and (From!="burjuman") and (From!="union") and (To!="burjuman") and (To!="union")):
    x=GreenLine.index(From)
    y=GreenLine.index(To)
    print From,"is",fabs(y-x),"stops from",To
if((From in GreenLine) and (To in RedLine) and (From!="burjuman") and (From!="union") and (To!="burjuman") and (To!="union")):
    x=GreenLine.index(From)
    y=RedLine.index(To)
    a=GreenLine.index("union")
    b=GreenLine.index("burjuman")
    if((fabs(a-x))>(fabs(b-x))):
        print "Interchange Station is",GreenLine[b]
        c=RedLine.index(GreenLine[b])
        print From,"via",GreenLine[b],"to",To,"is",(fabs(b-x)+fabs(c-y))
    if((fabs(b-x))>(fabs(a-x))):
        print "Interchange Station is",GreenLine[a]
        c=RedLine.index(GreenLine[a])
        print From,"via",GreenLine[a],"to",To,"is",(fabs(a-x)+fabs(c-y))
if((From in RedLine) and (To in GreenLine) and (From!="burjuman") and (From!="union") and (To!="burjuman") and (To!="union")):
    x=RedLine.index(From)
    y=GreenLine.index(To)
    a=RedLine.index("union")
    b=RedLine.index("burjuman")
    
    if((fabs(a-x))>(fabs(b-x))):
        print "Interchange Station is",RedLine[b]
        c=GreenLine.index(RedLine[b])
        print From,"via",GreenLine[b],"to",To,"is",(fabs(b-x)+fabs(c-y))
    if((fabs(b-x))>(fabs(a-x))):
        print "Interchange Station is",RedLine[a]
        c=GreenLine.index(RedLine[a])
        print From,"via",RedLine[a],"to",To,"is",(fabs(a-x)+fabs(c-y))

if(From=="burjuman" and To=="union"):
    print "union is 6 stops from burjuman"
if(From=="union" and To=="burjuman"):
    print "burjuman is 6 stops from union"
if(((From=="burjuman") or (From=="union")) and (To!="burjuman") and (To!="union") ):
    if(To in GreenLine):
        x=GreenLine.index(From)
        y=GreenLine.index(To)
        print From,"is",fabs(y-x),"stops from",To
    if(To in RedLine):
        x=RedLine.index(From)
        y=RedLine.index(To)
        print From,"is",fabs(y-x),"stops from",To
if(((To=="burjuman") or (To=="union")) and (From!="burjuman") and (From!="union")):
    if(From in GreenLine):
        x=GreenLine.index(From)
        y=GreenLine.index(To)
        print From,"is",fabs(y-x),"stops from",To
    if(From in RedLine):
        x=RedLine.index(From)
        y=RedLine.index(To)
        print From,"is",fabs(y-x),"stops from",To


    
    
