print"WELCOME TO OUR APPLICATION"
from Tkinter import *
import Tkinter as ttk 
from ttk import *
from math import *

import datetime
time=datetime.datetime.now()
import time
the_time=''
class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.instruction=Label(self,text="Metro Planner")
        self.instruction.grid(row=0,column=0,columnspan=2,sticky=W)
        self.ins2=Label(self,text="From")
        self.ins2.grid(row=1,column=0,columnspan=1,sticky=W)
        liststations={"Jebel Ali","Jebel Ali Industrial","Noor Islamic Bank","First Gulf Bank",
                          "Mall of the Emirates","Sharaf DG","Dubai Internet City","Nakheel","Dubai Marina","Jumeirah Lake Towers",
                          "Nakheel Harbor & Tower","Ibn Battuta","Energy","Business Bay",
                          "Burj Khalifa / Dubai Mall"," Dubai International Financial Centre ","Emirates Towers","Dubai World Trade Centre ","Al Jafiliya","Al Karama",
                          "Creek","Al Jaddaf","Dubai Healthcare City ","Oud Metha","Burjuman","Al Fahidi","Al Ghubaiba","Al Ras",
                          "Baniyas Square","Palm Deira","Union  Square","Al Rigga","Deira City Centre","GGICO","Airport Terminal-1","Airport Terminal-3",
                          "Emirates","Rashidiya ","Salahuddin","Abu Bakr Seddiq","Abu Hail",
                          "Al Qiyadah","Rashid Stadium","Al Nahda","Airport Free Zone","Al Qusais-1","Etisalat"}
        self.var1=StringVar()
        self.var2=StringVar()

        self.From=OptionMenu(self,self.var1,*liststations)
        self.var1.set('Select')
        self.From.grid(row=1,column=1,sticky=W)
        self.ins3=Label(self,text="To")
        self.ins3.grid(row=2,column=0,columnspan=1,sticky=W)
        self.To=OptionMenu(self,self.var2,*liststations)
        self.var2.set('Select')
        self.To.grid(row=2,column=1,columnspan=2,sticky=W)
        self.ins4=Label(self,text="CARD")
        self.ins4.grid(row=3,column=0,sticky=W)
        self.card=StringVar()
        self.radiobutton1=Radiobutton(self,text="gold",variable=self.card,value="gold").grid(row=4,column=0,sticky=W)
        self.radiobutton2=Radiobutton(self,text="silver",variable=self.card,value="silver").grid(row=4,column=1,sticky=W)
        self.radiobutton3=Radiobutton(self,text="blue",variable=self.card,value="blue").grid(row=5,column=0,sticky=W)
        self.radiobutton4=Radiobutton(self,text="red",variable=self.card,value="red").grid(row=5,column=1,sticky=W)
        self.submit_button=Button(self,text="Submit",command=self.bigprogram)
        self.submit_button.grid(row=6,column=0,columnspan=2,sticky=W)
        self.closebutton=Button(self,text="close",command=root.destroy)
        self.closebutton.grid(row=6,column=2)
        



        

        #Create a label that displays time:
        self.display_time=Label(self, text=the_time)
        self.display_time.grid(row=0, column=2)

        def change_value_the_time():
            global the_time
            newtime = time.strftime('%H:%M:%S')
            if newtime != the_time:
                the_time= newtime
                self.display_time.config(text=the_time, font="40")
            self.display_time.after(20, change_value_the_time)

        change_value_the_time()
        
        
        
        
        
    def bigprogram(self):
            From=self.var1.get()
            To=self.var2.get()
            cardtype=self.card.get()
            
            card=["gold","silver","blue","red"]
            zone1=["Jebel Ali","Jebel Ali Industrial"]
            zone2=["Noor Islamic Bank","First Gulf Bank","Mall of the Emirates","Sharaf DG","Dubai Internet City","Nakheel","Dubai Marina","Jumeirah Lake Towers","Nakheel Harbor & Tower","Ibn Battuta","Energy"]
            zone3=["Business Bay","Burj Khalifa / Dubai Mall"," Dubai International Financial Centre ","Emirates Towers","Dubai World Trade Centre ","Al Jafiliya","Al Karama","Creek","Al Jaddaf","Dubai Healthcare City ","Oud Metha","Burjuman","Al Fahidi","Al Ghubaiba"]
            zone4=["Al Ras","Baniyas Square","Palm Deira","Union  Square","Al Rigga","Deira City Centre","GGICO","Airport Terminal-1","Airport Terminal-3","Emirates","Rashidiya ","Salahuddin","Abu Bakr Seddiq","Abu Hail",
            "Al Qiyadah","Rashid Stadium","Al Nahda","Airport Free Zone","Al Qusais-1","Etisalat"]
            liststations=["Jebel Ali","Jebel Ali Industrial","Noor Islamic Bank","First Gulf Bank",
                          "Mall of the Emirates","Sharaf DG","Dubai Internet City","Nakheel","Dubai Marina","Jumeirah Lake Towers",
                          "Nakheel Harbor & Tower","Ibn Battuta","Energy","Business Bay",
                          "Burj Khalifa / Dubai Mall"," Dubai International Financial Centre ","Emirates Towers","Dubai World Trade Centre ","Al Jafiliya","Al Karama",
                          "Creek","Al Jaddaf","Dubai Healthcare City ","Oud Metha","Burjuman","Al Fahidi","Al Ghubaiba","Al Ras",
                          "Baniyas Square","Palm Deira","Union  Square","Al Rigga","Deira City Centre","GGICO","Airport Terminal-1","Airport Terminal-3",
                          "Emirates","Rashidiya ","Salahuddin","Abu Bakr Seddiq","Abu Hail",
                          "Al Qiyadah","Rashid Stadium","Al Nahda","Airport Free Zone","Al Qusais-1","Etisalat"]
            length=len(card)
            length1=len(zone1)
            length2=len(zone2)
            length3=len(zone3)
            length4=len(zone4)
            if ((From in liststations) and (To in liststations) and (cardtype in card)):
            

                if(cardtype=="gold"):
                    if (From==To):
                        print "IF YOU TAG OUT FROM SAME STATION IT WILL COST YOU MINIMUM AMOUNT:"
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
                        print "IF YOU TAG OUT FROM SAME STATION IT WILL COST YOU MINIMUM AMOUNT:"
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
                if(cardtype=="red"):
                    if (From==To):
                        print "IF YOU TAG OUT FROM SAME STATION IT WILL COST YOU MINIMUM AMOUNT:"
                        print "Aed.2.0"
                    elif ((From in zone1) and (To in zone1)):
                     a=zone1.index(From)
                     b=zone1.index(To)
                     if (b==a+1 or a==b+1):
                        print "Aed.2.0"
                     else:
                        print "Aed.2.5"

                    elif ((From in zone2) and (To in zone2)):
                        a=zone2.index(From)
                        b=zone2.index(To)
                        if (b==a+1 or a==b+1):
                         print "Aed.2.0"
                        else:
                         print"Aed.2.5"
                    elif ((From in zone3) and (To in zone3)):
                     a=zone3.index(From)
                     b=zone3.index(To)
                     if (b==a+1 or a==b+1):
                         print "Aed.2.0"
                     else:
                         print "Aed.2.5"
                        
                    elif ((From in zone4) and (To in zone4)):
                      a=zone4.index(From)
                      b=zone4.index(To)
                      if (b==a+1 or a==b+1):
                        print "Aed.2.0"
                      else:
                        print "Aed.2.5"
                    
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
                            print "price",":","Aed.4.5"
                       elif (r=="zone1" and s=="zone3"):
                            print "price",":","Aed.6.5"
                       elif (r=="zone1" and s=="zone4"):
                            print "price",":","Aed.6.5"
                       elif (r=="zone2" and s=="zone1"):
                            print "price",":","Aed.4.5"

                       elif (r=="zone2" and s=="zone3"):
                            print "price",":","Aed.4.5"
                       elif (r=="zone2" and s=="zone4"):
                            print "price",":","Aed.6.5"
                       elif (r=="zone3" and s=="zone1"):
                            print "price",":","Aed.6.5"
                       elif (r=="zone3" and s=="zone4"):
                            print "price",":","Aed.4.5"
                            
                       elif (r=="zone3" and s=="zone2"):
                            print "price",":","Aed.4.5"
                       elif (r=="zone4" and s=="zone1"):
                            print "price",":","Aed.6.5"
                       elif (r=="zone4" and s=="zone2"):
                            print "price",":","Aed.6.5"
                       elif (r=="zone4" and s=="zone3"):
                            print "price",":","Aed.4.5"
                if(cardtype=="blue"):
                    if (From==To):
                        print "IF YOU TAG OUT FROM SAME STATION IT WILL COST YOU MINIMUM AMOUNT:" 
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
                if (hour==23 and minute>28):
                    print "The next train will arrive at",5,":",45
                    
                if (From=="Dubai Healthcare City "):
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
                                break
                if (From=="Oud Metha"):
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
                                break
                if (From=="Jebel Ali"):
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
                                break
                if (From=="Al Qusais-1"):
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
                                break
                if (From=="Etisalat"):
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
                                break
                if (From=="Al Karama"):
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
                                break
                if (From=="Rashidiya "):
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
                                break
                if (From=="Burjuman"):
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
                                break
                if (From=="Al Fahidi"):
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
                                break
                if (From=="Al Ghubaiba"):
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
                                break

                if (From=="Al Jaddaf"):
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
                                break
                if (From=="Creek"):
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
                                break

                if (From=="Airport Free Zone"):
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
                                break
                if (From=="Al Jafiliya"):
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
                                break
                if (From=="Emirates Towers"):
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
                                break
                if (From=="Burj Khalifa / Dubai Mall"):
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
                                break
                if (From=="Business Bay"):
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
                                break
                if (From==" Dubai International Financial Centre "):
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
                                break
                if (From=="Dubai World Trade Centre "):
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
                                break
                if (From=="Palm Deira"):
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
                                break
                if (From=="Business Bay"):
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
                                break

                if (From=="Airport Terminal-3"):
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
                                break
                if (From=="GGICO"):
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
                                break
                if (From=="Abu Bakr Seddiq"):
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
                                break
                if (From=="Business Bay"):
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
                                break

                if (From=="Rashid Stadium"):
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
                                break

                if (From=="Baniyas Square"):
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
                                break

                if (From=="Airport Terminal-1"):
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
                                break


                if (From=="Emirates"):
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
                                break



                if (From=="Salahuddin"):
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
                                break
                                

                if (From=="Deira City Centre"):
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
                                break

                if (From=="Al Nahda"):
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
                                break
                if (From=="Al Qiyadah"):
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
                                break
                if (From=="Jebel Ali Industrial"):
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
                                break

                if (From=="Noor Islamic Bank"):
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
                                break
                  
                if (From=="Dubai Internet City"):
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
                                break
                if (From=="Dubai Marina"):
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
                                break
                   
                if (From=="Nakheel Harbor & Tower"):
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
                                break
                if (From=="First Gulf Bank"):
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
                                break
                if (From=="Energy"):
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
                                break
                if (From=="Sharaf DG"):
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
                                break
                if (From=="Al Rigga"):
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
                                break
                if (From=="Nakheel"):
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
                                break
                    
                if (From=="Union  Square"):
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
                                break
                if (From=="Ibn Battuta"):
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
                if (From=="Jumeirah Lake Towers"):
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
                                break
               
                RedLine=["Rashidiya ","Emirates","Airport Terminal-3","Airport Terminal-1","GGICO","Deira City Centre","Al Rigga","Union  Square","Burjuman","Al Karama",
                "Al Jafiliya","Dubai World Trade Centre ","Emirates Towers"," Dubai International Financial Centre ","Burj Khalifa / Dubai Mall","Business Bay","Noor Islamic Bank",
                "First Gulf Bank","Mall of the Emirates","Sharaf DG","Dubai Internet City","Nakheel","Dubai Marina","Jumeirah Lake Towers","Nakheel Harbor & Tower",
                "Ibn Battuta","Energy","Jebel Ali Industrial","Jebel Ali"]
                GreenLine=["Etisalat","Al Qusais-1","Airport Free Zone","Al Nahda,Rashid Stadium","Al Qiyadah","Abu Bakr Seddiq","Salahuddin","Union  Square","Baniyas Square",
                "Palm Deira","Al Ras","Al Ghubaiba","Al Fahidi","Burjuman","Oud Metha","Dubai Healthcare City ","Al Jaddaf","Creek"]
                Via=["Union  Square","Burjuman"]
                print "THE NUMBER OF STATIONS AND INTERCHANGE STATION IS:"
                if((From in RedLine) and (To in RedLine) and (From!="Burjuman") and (From!="Union  Square") and (To!="Burjuman") and (To!="Union  Square")):
                    x=RedLine.index(From)
                    y=RedLine.index(To)
                    print From,"is",fabs(y-x),"stops from",To
                if((From in GreenLine) and (To in GreenLine) and (From!="Burjuman") and (From!="Union  Square") and (To!="Burjuman") and (To!="Union  Square")):
                    x=GreenLine.index(From)
                    y=GreenLine.index(To)
                    print From,"is",fabs(y-x),"stops from",To
                if((From in GreenLine) and (To in RedLine) and (From!="Burjuman") and (From!="Union  Square") and (To!="Burjuman") and (To!="Union  Square")):
                    x=GreenLine.index(From)
                    y=RedLine.index(To)
                    a=GreenLine.index("Union  Square")
                    b=GreenLine.index("Burjuman")
                    if((fabs(a-x))>(fabs(b-x))):
                        print "Interchange Station is",GreenLine[b]
                        c=RedLine.index(GreenLine[b])
                        print From,"via",GreenLine[b],"to",To,"is",(fabs(b-x)+fabs(c-y))
                    if((fabs(b-x))>(fabs(a-x))):
                        print "Interchange Station is",GreenLine[a]
                        c=RedLine.index(GreenLine[a])
                        print From,"via",GreenLine[a],"to",To,"is",(fabs(a-x)+fabs(c-y))
                if((From in RedLine) and (To in GreenLine) and (From!="Burjuman") and (From!="Union  Square") and (To!="Burjuman") and (To!="Union  Square")):
                    x=RedLine.index(From)
                    y=GreenLine.index(To)
                    a=RedLine.index("Union  Square")
                    b=RedLine.index("Burjuman")
                    
                    if((fabs(a-x))>(fabs(b-x))):
                        print "Interchange Station is",RedLine[b]
                        c=GreenLine.index(RedLine[b])
                        print From,"via",GreenLine[b],"to",To,"is",(fabs(b-x)+fabs(c-y))
                    if((fabs(b-x))>(fabs(a-x))):
                        print "Interchange Station is",RedLine[a]
                        c=GreenLine.index(RedLine[a])
                        print From,"via",RedLine[a],"to",To,"is",(fabs(a-x)+fabs(c-y))

                if(From=="Burjuman" and To=="Union  Square"):
                    print "Union  Square is 6 stops from Burjuman"
                if(From=="Union  Square" and To=="Burjuman"):
                    print "Burjuman is 6 stops from Union  Square"
                if(((From=="Burjuman") or (From=="Union  Square")) and (To!="Burjuman") and (To!="Union  Square") ):
                    if(To in GreenLine):
                        x=GreenLine.index(From)
                        y=GreenLine.index(To)
                        print From,"is",fabs(y-x),"stops from",To
                    if(To in RedLine):
                        x=RedLine.index(From)
                        y=RedLine.index(To)
                        print From,"is",fabs(y-x),"stops from",To
                if(((To=="Burjuman") or (To=="Union  Square")) and (From!="Burjuman") and (From!="Union  Square")):
                    if(From in GreenLine):
                        x=GreenLine.index(From)
                        y=GreenLine.index(To)
                        print From,"is",fabs(y-x),"stops from",To
                    if(From in RedLine):
                        x=RedLine.index(From)
                        y=RedLine.index(To)
                        print From,"is",fabs(y-x),"stops from",To 
                if (To=="Dubai Healthcare City "):
                    print "The feeder buses available are:"
                    print "22-Healthcare city-Al Nahda 1"
                    print "42-GHUBAIBA BUS STATION :Al Ghubaiba 1"
                    print "C7-HOR AL ANZ BUS STATION-HEALTHCARE CITY"
                if (To=="Rashidiya "):
                    print "The feeder buses available are:"
                    print "F1- Ras Al Khor"
                    print "F2-Mirdif West"
                    print "F5-Al Mizhar"
                    print "F10-Al Warqa"
                    print "365-International City"
                if(To=="Emirates"):
                    print "The feeder buses available are:"
                    print "F8-Al Nahda 2"
                    print "Mamzar,Century Mall"
                if(To=="Airport Terminal-3"):
                    print "The feeder buses available are:"
                    print "C1-Satwa Bus Station"
                    print "88-Nakheel MS"
                if(To=="Airport Terminal-1"):
                    print "The feeder buses available are:"
                    print "C1-Satwa Bus Station"
                    print "4-Gold Souq Bus Station-Rashidiya  MS"
                    print "11A-Gold souq Bus Station-Al Awir Terminus"
                    print "32C-Al Qusais-1 Bus Station-Satwa Bus Station"
                    print "33-Ghubaiba Bus Station-Al Qusais-1 Bus Station"
                    print "42-Ghubaiba Bus Station-Airport Airport Terminal-1"
                    print "48-Mamzar,Century Mall-Rashidiya  MS"
                    print "64A-Glod Souk Bus Station-Ras Al Khor"
                    print "88-Airport Airport Terminal-3-Nakheel MS"
                if(To=="GGICO"):
                    print "The feeder buses available are:"
                    print "42-Ghubaiba Bus Station-airport Airport Terminal-1"
                if(To=="Deira City Centre"):
                    print "The feeder buses available are:"
                    print "C10-Hamriya Port- Jumeirah Beach Park"
                    print "C14-Mamzar,Century Mall-Safa Terminus"
                    print "C15-Hamriya Port-Al Wasl Park Terminus"
                    print "C19-Ghubaiba Bus Station-Al Qusais-1 Industrial Area"
                    print "X28-Lulu Village-Nakheel MS"
                    print "22-Health Care City-Al Nahda 1"  
                    print "27-Gold Souq Bus Station-Dubai Mall"
                    print "33-Ghubaiba Bus Station-Al Qusais-1 Bus Station"
                    print "53-Ghubaiba Bus Station-International City"
                    print "88-Airport Airport Terminal-3-Nakhell MS"
                if(To=="Al Rigga"):
                    print "The feeder buses available are:"
                    print "C9-Satwa Bus Station-Hor Al Anz East"
                if(To=="Union  Square"):
                    print "The feeder buses available are:"
                    print "C1-Airport Airport Terminal-3-Satwa Bus Station"
                    print "C2-Zabeel Park-Airport Terminal 2"
                    print "C4-Gold Souq Bus Station-Jadaf"
                    print "C5-Gold Souq bus Station-Ghubaiab Bus Satation"
                    print "C7-Hor Al Anz Bus Station-Healthcare City"
                    print "C9-Satwa Bus Station-Hor Al Anz East "
                    print "C28-Gold Souq Bus Station-Mamzar Beach Park"
                    print "C55-Gold Souq Bus Station-Ghubaiba Bus Station"
                    print "E303-Union  Square Square MS-Sharjah"
                    print "E700-Fujairah-Union  Square Square MS"
                    print "E400-Union  Square Square MS-Ajman"
                    print "X94-Gold Souq Bus Station-Dubai Investment Park"
                    print "4-Gold Souq Bus Station-Rashidiya  MS"
                    print "11A-Gold Souq Bus Station-Al Awir Terminus"
                    print "27-Gold Souq Bus Station-Dubai Mall"
                    print "64A-Gold Souq Bus Station-Ras Al Khor"
                if(To=="Burjuman"):
                    print "The feeder buses available are:"
                    print "C2-Zabeel Park-Airport Terminal 2"
                    print "C3-Hor Al Anz Bus Station-Karama Bus Station"
                    print "C5-Gold Souq Bus Station-Ghubaiba Bus Station"
                    print "C10-Hamriya Port-Jumeirah Beach Park"
                    print "C18-Shaikh Rashid Colony,AlQusais-Lamcy Plaza"    
                    print "C19-Ghubaiba Bus Station-Al Qusais-1 Industrial Area"
                    print "C55-Gold Souq Bus Station-Ghubaiba Bus Station"
                    print "X23-Gold Souq Bus Station–International City" 
                    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4"
                    print "33-Ghubaiba Bus Station–Al Qusais-1 Bus Station" 
                    print "42-Ghubaiba Bus Station–Airport Airport Terminal-1"
                    print "44-Ghubaiba Bus Station–Dubai Festival City"
                    print "61-Ghubaiba Bus Station–Ras Al Khor" 
                    print "61D-Ghubaiba Bus Station–Nad Al Sheba Clinic" 
                    print "66-Ghubaiba Bus Station–Faqa Terminus"
                    print "67-Ghubaiba Bus Station–Endurance City Terminus"
                    print "91-Ghubaiba Bus Station–Jebel Ali Bus Station"
                if(To=="Al Karama"):
                    print "The feeder buses available are:"
                    print "C2-Airport Terminal 2–Zabeel Park"
                    print "C10-Hamriya Port–Jumeirah Beach Park"
                    print "C15 Hamriya Port–Al Wasl Park"
                    print "C26-Al Wasl Park–Al Qusais-1 Industrial Area"
                    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4"
                    print "61-Ghubaiba Bus Station–Ras Al Khor Industrial Area"
                    print "88-Airport Airport Terminal-3–Nakheel MS"
                if(To=="Al Jafiliya"):
                    print "The feeder buses available are:"
                    print "C2-Zabeel Park–Airport Terminal 2"
                    print "C15-Hamriya Port–Al Wasl Park Terminus"
                    print "C26-Al Wasl Park Terminus–Al Qusais-1 Industrial Area"
                    print "X10-Gold Souq Bus Station–Al Quoz Bus Station" 
                    print "X28-Lulu Village–Nakheel MS" 
                    print "X92-Ghubaiba Bus Station–Dubai Investment Park"
                    print "10-Gold Souq Bus Station–Al Quoz Bus Station" 
                    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4" 
                    print "27-Gold Souq Bus Station-Dubai Mall" 
                    print "61-Ghubaiba Bus Station–Ras Al Khor Ind. Area" 
                    print "88-Airport Airport Terminal-3–Nakheel MS"
                if(To=="Dubai World Trade Centre "):
                    print "The feeder buses available are:"
                    print "F11-Financial Centre MS–Satwa"
                    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4" 
                    print "98E-Satwa Bus Station–Al Quoz Ind. Area 3"
                if(To=="Emirates Towers"):
                    print "The feeder buses available are:"
                    print "F11 Financial Centre MS – Satwa"
                    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4"
                    print "27-Gold Souq Bus Station–Dubai Mall"
                    print "98E-Satwa Bus Station–Al Quoz Ind. Area 3"
                if(To==" Dubai International Financial Centre "):
                    print "The feeder buses available are:"
                    print "F11-Financial Centre MS–Satwa" 
                if(To=="Burj Khalifa / Dubai Mall"):
                    print "The feeder buses available are:"
                    print "F13-Burj Khalifa/Dubai Mall MS–Dubai Mall"
                    print "F16-Burj Khalifa/Dubai Mall MS–Jumeirah 2"
                if(To=="Business Bay"):
                    print "The feeder buses available are:"
                    print "F16 Dubai Mall – Jumeirah 2" 
                    print "F20 Business Bay MS – Al Safa 1"
                    print "7-Ghubaiba Bus Station–Iranian Clinic Al Quoz"
                if(To=="Noor Islamic Bank"):
                    print "The feeder buses available are:"
                    print "F15-Noor Islamic Bank MS–Al Quoz Ind. Area 2"
                    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4"
                if(To=="First Gulf Bank"):
                    print "The feeder buses available are:"
                    print "F25-First Gulf Bank MS land side–Al Quoz 3 & 4"
                    print "12-Ghubaiba Bus Station–Al Quoz Bus Station"
                if(To=="Mall of the Emirates"):
                    print "The feeder buses available are:"
                    print "F30-Mall of the Emirates MS–Arabian Ranches"
                    print "F33-Mall of the Emirates MS–Al Barsha 3" 
                    print "93-Ghubaiba Bus Station–The Greens"
                if(To=="Dubai Internet City"):
                    print "The feeder buses available are:"
                    print "F31-The Meadows–Dubai Internet City MS"
                    print "88-Airport Airport Terminal-3–Nakheel MS"
                    print "X28-Lulu Village–Nakheel MS" 
                if(To=="Nakheel"):
                    print "The feeder buses avaliable are:"
                    print "X28-Lulu Village-Nakheel MS"
                    print "88-Airport Airport Terminal-3–Nakheel MS"
                if(To=="Dubai Marina"):
                    print "The feeder buses avaliable are:"
                    print "F37-Marina MS–Dubai Marina"
                if(To=="Jumeirah Lake Towers"):
                    print "The feeder buses available are:"
                    print "F37-Marina MS–Jumeirah Lakes Tower MS–Dubai Marina"
                if(To=="Ibn Battuta"):
                    print "The feeder buses avaliable are:"
                    print "E101-Abu Dhabi–Ibn Batutta"
                    print "F43-Ibn Battuta MS–Discovery Gardens"
                    print "F44-Ibn Battuta MS–The Gardens"
                    print "F46-Ibn Battuta MS–IMP Zone"
                    print "F48-Ibn Battuta MS–Dubai Investment Park"
                    print "F53-Ibn Battuta MS–Dubai Industrial City"
                    print "8-Ibn Battuta MS–Gold Souk Bus Station"
                if(To=="Jebel Ali"):
                    print "The feeder buses avaliable are:"
                    print "F54-Jafza South–Jebel Ali MS"
                    print "99-New East Camp–Marine Control Towers"
                if(To=="Jebel Ali Industrial"):
                    print "The feeder buses avaliable are:"
                    print "F54-Jafza South–Jebel Ali MS"
                    print "99-New East Camp–Marine Control Towers"
                    

                    
                if(To=="Etisalat"):
                    print "The feeder buses avaliable are:"
                    print "31-Gold Souq Bus Station–Oud Al Mateena"
                if(To=="Al Qusais-1"):
                    print "The feeder buses avaliable are:"
                    print "13 Gold Souq Bus Station – Al Qusais-1 Bus Station"
                    print "31-Gold Souq Bus Station–Oud Al Mateena"
                    print "64-Gold Souq Bus Station–Ras Al Khor"
                if(To=="Airport Free Zone"):
                    print "The feeder buses avaliable are:"
                    print "13-Gold Souq Bus Station–Al Qusais-1 Bus Station"
                    print "17-Al Sabkha Bus Station–Al Qusais-1 Bus Station" 
                    print "31-Gold Souq Bus Station–Oud Al Mateena"
                    print "64-Gold Souq Bus Station–Ras Al Khor"
                    print "C18-Shaikh Rashid Colony, Al Qusais-1–Lamcy Plaza" 
                    print "C19-Ghubaiba Bus Station–Al Qusais-1 Industrial Area"
                    print "x28-Lulu Village–Nakheel MS"
                if(To=="Al Nahda"):
                    print "The feeder buses avaliable are:"
                    print "13 Gold Souq Bus Station–Al Qusais-1 Bus Station"
                    print "13A Gold Souq Bus Station–Al Qusais-1 Bus Station"
                    print "17 Al Sabkha Bus Station–Al Qusais-1 Bus Station"
                    print "22 Healthcare City–Al Nahda 1"
                    print "31 Gold Souq Bus Station–Oud Al Mateena"
                    print "64 Gold Souq Bus Station–Ras Al Khor"
                    print "C18 Shaikh Rashid Colony, Al Qusais-1–Lamcy Plaza"
                    print "C19 Ghubaiba Bus Station–Al Qusais-1 Industrial Area"
                    print "X28 Lulu Village–Nakheel MS"
                if(To=="Rashid Stadium"):
                    print "The feeder buses available are:"
                    print "13-Gold Souq Bus Station–Al Qusais-1 Bus Station"
                    print "13A Gold Souq Bus Station–Al Qusais-1 Bus Station"
                    print "17 Al Sabkha Bus Station–Al Qusais-1 Bus Station"
                    print "22 Healthcare City–Al Nahda 1"
                    print "64 Gold Souq Bus Station–Ras Al Khor"
                    print "C18 Shaikh Rashid Colony, Al Qusais-1–Lamcy Plaza"
                    print "C19 Ghubaiba Bus Station–Al Qusais-1 Industrial Area"
                    print "X28 Lulu Village–Nakheel MS"
                if(To=="Al Qiyadah"):
                    print "The feeder buses available are:"
                    print "C9-Al Satwa Bus Station–Hor Al Anz East"
                if(To=="Abu Hail"):
                    print "The feeder buses available are:"
                    print "13 Gold Souq Bus Station–Al Qusais-1 Bus Station"
                    print "13A Gold Souq Bus Station–Al Qusais-1 Bus Station"
                    print "48 Mamzar, Century Mall–Al Rashidiya  MS"
                    print "C2 Zabeel Park–Airport Terminal 2"
                    print "C3 Hor Al Anz Bus Station–Karama Bus Station"
                    print "C7 Hor Al Anz Bus Station–Healthcare City"
                    print "C9 Satwa Bus Station–Hor Al Anz East"
                    print "C19 Ghubaiba Bus Station–Al Qusais-1 Industrial Area"
                    print "X28 Lulu Village–Nakheel MS"
                if(To=="Abu Bakr Seddiq"):
                    print "The feeder buses available are:"
                    print "13 Gold Souq Bus Station–Al Qusais-1 Bus Station"
                    print "13A Gold Souq Bus Station–Al Qusais-1 Bus Station"
                    print "48 Mamzar, Century Mall–Al Rashidiya  MS"
                    print "C2 Zabeel Park–Airport Terminal 2"
                    print "C19 Ghubaiba Bus Station–Al Qusais-1 Industrial Area" 
                    print "x28 Lulu Village–Nakheel MS" 
                if(To=="Salahuddin"):
                    print "The feeder buses available are:"
                    print "10-Gold Souq Bus Station–Al Quoz Bus Station"
                    print "13-Gold Souq Bus Station–Al Qusais-1 Bus Station"
                    print "13A-Gold Souq Bus Station–Al Qusais-1 Bus Station"
                    print "C2-Zabeel Park–Airport Terminal 2"
                    print "C28-Gold Souq Bus Station–Mamzar Beach Park"
                
                if(To=="Baniyas Square"):
                    print "The feeder buses available are:"
                    print "17-Al Sabkha Bus Station–Al Qusais-1 Bus Station" 
                    print "64A-Gold Souq Bus Station–Ras Al Khor"
                if(To=="Palm Deira"):
                    print "The feeder buses available are:"
                    print "8-Gold Souq Bus Station–Al Mina Al Siyahi" 
                    print "C1-Airport Airport Terminal-3–Satwa Bus Station"
                    print "C2-Zabeel Park–Airport Terminal 2" 
                    print "C3-Hor Al Anz Bus Station-Karama Bus Station" 
                    print "C7-Hor Al Anz Bus Station–Healthcare City"
                    print "C9-Satwa Bus Station–Hor Al Anz East"
                    print "C18-Shaikh Rashid Colony, Al Qusais-1–Lamcy Plaza"
                    print "C55-Gold Souq Bus Station–Ghubaiba Bus Station"
                    print "X10-Gold Souq Bus Station–Al Qouz Bus Station"
                    print "X13-LuLu Village–Al Satwa Bus Station"
                    print "X23-Gold Souq Bus Station–International City"
                if(To=="Al Ras"):
                    print "The feeder buses available are:"
                    print "27-Gold Souq Bus Station–Dubai Mall"
                    print "53-Ghubaiba Bus Station–International City"
                    print "C2-Zabeel Park–Airport Terminal 2"
                    print "C4-Gold Souq Bus Station–Jadaf"
                    print "C7-Hor Al Anz Bus Station–Healthcare City"
                    print "C9-Satwa Bus Station–Hor Al Anz East"
                    print "C28-Gold Souq Bus Station–Mamzar Beach Park"
                    print "C55-Gold Souq Bus Station–Ghubaiba Bus Station"
                if(To=="Al Ghubaiba"):
                    print "The feeder buses available are:"
                    print "8-Gold Souq Bus Station–Al Mina Al Siyahi"
                    print "C5-Gold Souq Bus Station–Ghubaiba Bus Station"
                    print "C7-Hor Al Anz Bus Station–Healthcare City"
                    print "C9-Satwa Bus Station–Hor Al Anz East"
                    print "X13-LuLu Village–Al Satwa Bus Station"    
                if(To=="Al Fahidi"):
                    print "The feeder buses available are:"
                    print "21-Ghubaiba Bus Station–Al Quoz Ind. Area 4"
                    print "33-Ghubaiba Bus Station–Qusais Bus Station"
                    print "42-Ghubaiba Bus Station–Airport Airport Terminal-1" 
                    print "44-Ghubaiba Bus Station–Dubai Festival City" 
                    print "61-Ghubaiba Bus Station–Ras Al Khor"
                    print "61D-Ghubaiba Bus Station-Nad Al Sheba Clinic"
                    print "66-Ghubaiba Bus Station–Faqa Terminus"
                    print "67-Ghubaiba Bus Station–Endurance City Terminus"
                    print "91-Ghubaiba Bus Station–Jebel Ali Bus Station"
                    print "C1-Airport Airport Terminal-3–Satwa Bus Station"
                    print "C2-Zabeel Park–Airport Terminal 2"
                    print "C3-Hor Al Anz Bus Station–Karama Bus Station"
                    print "C5-Gold Souq Bus Station–Ghubaiba Bus Station"
                    print "C7-Hor Al Anz Bus Station–Healthcare City"
                    print "C18-Shaikh Rashid Colony, Al Qusais-1–Lamcy Plaza"
                    print "C19-Ghubaiba Bus Station-Al Qusais-1 Industrial Area"
                    print "C55-Gold Souq Bus Station-Ghubaiba Bus Station"
                    print "X23-Gold Souq Bus Station–International City"
                if(To=="Oud Metha"):
                    print "The feeder buses available are:"
                    print "22-Healthcare City – Al Nahda 1"
                    print "42-Ghubaiba Bus Station-Airport Airport Terminal-1"
                    print "44-Ghubaiba Bus Station-Dubai Festival City"
                    print "61D-Ghubaiba Bus Station-Nad Al Sheba Clinic"
                    print "66-Ghubaiba Bus Station-Faqa Terminus"
                    print "67-Ghubaiba Bus Station-Endurance City Terminus"
                    print "C4-Gold Souq Bus Station-Jadaf"
                    print "C7-Hor Al Anz Bus Station-Healthcare City"
                    print "C18-Shaikh Rashid Colony, Al Qusais-1-Lamcy Plaza"
                    print "X23-Gold Souq Bus Station–International City"
            elif((From not in liststations) and (To not in liststations)):
                print "YOUR STARTING AND DESTINATION STATION AND CARDTYPE IS NOT FOUND"
            elif((From not in liststations) and (To not in liststations)):
                print "YOUR STARTING AND DESTINATION STATION IS NOT FOUND"
            elif((From not in liststations) and (cardtype not in card)):
                print "YOUR STARTING STATION AND CARDTYPE NOT FOUND"
            elif((To not in liststations) and (cardtype not in card)):
                print "YOUR DESTINATION STATION AND CARDTYPE NOT FOUND"
            elif(cardtype not in card):
                print "CARDTYPE IS NOT FOUND"
            elif(From not in liststations):
                print "YOUR STARTING STATION IS NOT FOUND"

            elif(To not in liststations):
                print "YOUR DESTINATION STATION IS NOT FOUND"
            
       
root=Tk()
p = PhotoImage(file="G:\pythonimg.gif")
l = Label(root, image=p)

l.pack_propagate(0)
l.pack()
l.grid()



root.option_add("*background","white")
root.configure(background='blue')
root.title("metro planner")
root.geometry("275x375")
app=Application(root)
app.grid()
root.mainloop()




            
