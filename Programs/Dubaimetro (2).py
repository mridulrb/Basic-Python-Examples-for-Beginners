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
                          "Creek","Al Jaddaf","Dubai Healthcare City","Oud Metha","Burjuman","Al Fahidi","Al Ghubaiba","Al Ras",
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
        self.radiobutton1=Radiobutton(self,text="Gold",variable=self.card,value="Gold").grid(row=4,column=0,sticky=W)
        self.radiobutton2=Radiobutton(self,text="Silver",variable=self.card,value="Silver").grid(row=4,column=1,sticky=W)
        self.radiobutton3=Radiobutton(self,text="Blue",variable=self.card,value="Blue").grid(row=5,column=0,sticky=W)
        self.radiobutton4=Radiobutton(self,text="Red",variable=self.card,value="Red").grid(row=5,column=1,sticky=W)
        self.submit_button=Button(self,text="Submit",command=self.bigprogram)
        self.submit_button.grid(row=6,column=0,columnspan=2,sticky=W)
        self.closebutton=Button(self,text="close",command=root.destroy)
        self.closebutton.grid(row=6,column=2)
        self.text=Text(self,width=50,height=2,wrap=WORD)
        self.text.grid(row=7,column=0,columnspan=2,sticky=W)
        self.text2=Text(self,width=50,height=2,wrap=WORD)
        self.text2.grid(row=8,column=0,columnspan=4,sticky=W)
        self.text3=Text(self,width=50,height=2,wrap=WORD)
        self.text3.grid(row=9,column=0,columnspan=4,sticky=W)
        
        
        
        



        

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
            
            card=["Gold","Silver","Blue","Red"]
            zone1=["Jebel Ali","Jebel Ali Industrial"]
            zone2=["Noor Islamic Bank","First Gulf Bank","Mall of the Emirates","Sharaf DG","Dubai Internet City","Nakheel","Dubai Marina","Jumeirah Lake Towers","Nakheel Harbor & Tower","Ibn Battuta","Energy"]
            zone3=["Business Bay","Burj Khalifa / Dubai Mall"," Dubai International Financial Centre ","Emirates Towers","Dubai World Trade Centre ","Al Jafiliya","Al Karama","Creek","Al Jaddaf","Dubai Healthcare City","Oud Metha","Burjuman","Al Fahidi","Al Ghubaiba"]
            zone4=["Al Ras","Baniyas Square","Palm Deira","Union  Square","Al Rigga","Deira City Centre","GGICO","Airport Terminal-1","Airport Terminal-3","Emirates","Rashidiya ","Salahuddin","Abu Bakr Seddiq","Abu Hail",
            "Al Qiyadah","Rashid Stadium","Al Nahda","Airport Free Zone","Al Qusais-1","Etisalat"]
            liststations=["Jebel Ali","Jebel Ali Industrial","Noor Islamic Bank","First Gulf Bank",
                          "Mall of the Emirates","Sharaf DG","Dubai Internet City","Nakheel","Dubai Marina","Jumeirah Lake Towers",
                          "Nakheel Harbor & Tower","Ibn Battuta","Energy","Business Bay",
                          "Burj Khalifa / Dubai Mall"," Dubai International Financial Centre ","Emirates Towers","Dubai World Trade Centre ","Al Jafiliya","Al Karama",
                          "Creek","Al Jaddaf","Dubai Healthcare City","Oud Metha","Burjuman","Al Fahidi","Al Ghubaiba","Al Ras",
                          "Baniyas Square","Palm Deira","Union  Square","Al Rigga","Deira City Centre","GGICO","Airport Terminal-1","Airport Terminal-3",
                          "Emirates","Rashidiya ","Salahuddin","Abu Bakr Seddiq","Abu Hail",
                          "Al Qiyadah","Rashid Stadium","Al Nahda","Airport Free Zone","Al Qusais-1","Etisalat"]
            length=len(card)
            length1=len(zone1)
            length2=len(zone2)
            length3=len(zone3)
            length4=len(zone4)
            if ((From in liststations) and (To in liststations) and (cardtype in card)):
            

                if(cardtype=="Gold"):
                    if (From==To):
                        message= "IF YOU TAG OUT FROM SAME STATION IT WILL COST YOU MINIMUM AMOUNT: AED.3.6"
                        
                    elif ((From in zone1) and (To in zone1)):
                        a=zone1.index(From)
                        b=zone1.index(To)
                        if (b==a+1 or a==b+1):
                            message= "Aed.3.6"
                        else:
                            message= "Aed.4.6"

                    elif ((From in zone2) and (To in zone2)):
                        a=zone2.index(From)
                        b=zone2.index(To)
                        if (b==a+1 or a==b+1):
                            message= "Aed.3.6"
                        else:
                            message="Aed.4.6"
                    elif ((From in zone3) and (To in zone3)):
                        a=zone3.index(From)
                        b=zone3.index(To)
                        if (b==a+1 or a==b+1):
                            message= "Aed.3.6"
                        else:
                            message= "Aed.4.6"
                        
                    elif ((From in zone4) and (To in zone4)):
                        a=zone4.index(From)
                        b=zone4.index(To)
                        if (b==a+1 or a==b+1):
                            message= "Aed.3.6"
                        else:
                            message= "Aed.4.6"
                
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
                            message= "price",":","Aed.8.2"
                        elif (r=="zone1" and s=="zone3"):
                            message= "price",":","Aed.11.6"
                        elif (r=="zone1" and s=="zone4"):
                            message= "price",":","Aed.11.6"
                        elif (r=="zone2" and s=="zone1"):
                            message= "price",":","Aed.8.2"

                        elif (r=="zone2" and s=="zone3"):
                            message= "price",":","Aed.8.2"
                        elif (r=="zone2" and s=="zone4"):
                            message= "price",":","Aed.11.6"
                        elif (r=="zone3" and s=="zone1"):
                            message= "price",":","Aed.11.6"
                        elif (r=="zone3" and s=="zone4"):
                            message= "price",":","Aed.8.2"
                            
                        elif (r=="zone3" and s=="zone2"):
                            message= "price",":","Aed.8.2"
                        elif (r=="zone4" and s=="zone1"): 
                            message= "price",":","Aed.11.6"
                        elif (r=="zone4" and s=="zone2"):
                            message= "price",":","Aed.11.6"
                        elif (r=="zone4" and s=="zone3"):
                            message= "price",":","Aed.8.2"
                
                if(cardtype=="Silver"):
                    if (From==To):
                        message= "IF YOU TAG OUT FROM SAME STATION IT WILL COST YOU MINIMUM AMOUNT: AED.1.8"
                    elif ((From in zone1) and (To in zone1)):
                     a=zone1.index(From)
                     b=zone1.index(To)
                     if (b==a+1 or a==b+1):
                        message= "Aed.1.8"
                     else:
                        message= "Aed.2.3"

                    elif ((From in zone2) and (To in zone2)):
                        a=zone2.index(From)
                        b=zone2.index(To)
                        if (b==a+1 or a==b+1):
                         message= "Aed.1.8"
                        else:
                         message="Aed.2.3"
                    elif ((From in zone3) and (To in zone3)):
                     a=zone3.index(From)
                     b=zone3.index(To)
                     if (b==a+1 or a==b+1):
                         message= "Aed.1.8"
                     else:
                         message= "Aed.2.3"
                        
                    elif ((From in zone4) and (To in zone4)):
                      a=zone4.index(From)
                      b=zone4.index(To)
                      if (b==a+1 or a==b+1):
                        message= "Aed.1.8"
                      else:
                        message= "Aed.2.3"
                    
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
                            message= "price",":","Aed.4.1"
                       elif (r=="zone1" and s=="zone3"):
                            message= "price",":","Aed.5.8"
                       elif (r=="zone1" and s=="zone4"):
                            message= "price",":","Aed.5.8"
                       elif (r=="zone2" and s=="zone1"):
                            message= "price",":","Aed.4.1"

                       elif (r=="zone2" and s=="zone3"):
                            message= "price",":","Aed.4.1"
                       elif (r=="zone2" and s=="zone4"):
                            message= "price",":","Aed.5.8"
                       elif (r=="zone3" and s=="zone1"):
                            message= "price",":","Aed.5.8"
                       elif (r=="zone3" and s=="zone4"):
                            message= "price",":","Aed.4.1"
                            
                       elif (r=="zone3" and s=="zone2"):
                            message= "price",":","Aed.4.1"
                       elif (r=="zone4" and s=="zone1"):
                            message= "price",":","Aed.5.8"
                       elif (r=="zone4" and s=="zone2"):
                            message= "price",":","Aed.5.8"
                       elif (r=="zone4" and s=="zone3"):
                            message= "price",":","Aed.4.1"
                if(cardtype=="Red"):
                    if (From==To):
                        message= "IF YOU TAG OUT FROM SAME STATION IT WILL COST YOU MINIMUM AMOUNT: AED.2.0"
                    elif ((From in zone1) and (To in zone1)):
                     a=zone1.index(From)
                     b=zone1.index(To)
                     if (b==a+1 or a==b+1):
                        message= "Aed.2.0"
                     else:
                        message= "Aed.2.5"

                    elif ((From in zone2) and (To in zone2)):
                        a=zone2.index(From)
                        b=zone2.index(To)
                        if (b==a+1 or a==b+1):
                         message= "Aed.2.0"
                        else:
                         message="Aed.2.5"
                    elif ((From in zone3) and (To in zone3)):
                     a=zone3.index(From)
                     b=zone3.index(To)
                     if (b==a+1 or a==b+1):
                         message= "Aed.2.0"
                     else:
                         message= "Aed.2.5"
                        
                    elif ((From in zone4) and (To in zone4)):
                      a=zone4.index(From)
                      b=zone4.index(To)
                      if (b==a+1 or a==b+1):
                        message= "Aed.2.0"
                      else:
                        message= "Aed.2.5"
                    
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
                            message= "price",":","Aed.4.5"
                       elif (r=="zone1" and s=="zone3"):
                            message= "price",":","Aed.6.5"
                       elif (r=="zone1" and s=="zone4"):
                            message= "price",":","Aed.6.5"
                       elif (r=="zone2" and s=="zone1"):
                            message= "price",":","Aed.4.5"

                       elif (r=="zone2" and s=="zone3"):
                            message= "price",":","Aed.4.5"
                       elif (r=="zone2" and s=="zone4"):
                            message= "price",":","Aed.6.5"
                       elif (r=="zone3" and s=="zone1"):
                            message= "price",":","Aed.6.5"
                       elif (r=="zone3" and s=="zone4"):
                            message= "price",":","Aed.4.5"
                            
                       elif (r=="zone3" and s=="zone2"):
                            message= "price",":","Aed.4.5"
                       elif (r=="zone4" and s=="zone1"):
                            message= "price",":","Aed.6.5"
                       elif (r=="zone4" and s=="zone2"):
                            message= "price",":","Aed.6.5"
                       elif (r=="zone4" and s=="zone3"):
                            message= "price",":","Aed.4.5"
                if(cardtype=="Blue"):
                    if (From==To):
                        message= "IF YOU TAG OUT FROM SAME STATION IT WILL COST YOU MINIMUM AMOUNT: AED.0.9"
                    elif ((From in zone1) and (To in zone1)):
                     a=zone1.index(From)
                     b=zone1.index(To)
                     if (b==a+1 or a==b+1):
                        message= "Aed.0.9"
                     else:
                        message= "Aed.1.05"

                    elif ((From in zone2) and (To in zone2)):
                     a=zone2.index(From)
                     b=zone2.index(To)
                     if (b==a+1 or a==b+1):
                        message= "Aed.0.9"
                     else:
                        message="Aed.1.05"
                    elif ((From in zone3) and (To in zone3)):
                     a=zone3.index(From)
                     b=zone3.index(To)
                     if (b==a+1 or a==b+1):
                        message= "Aed.0.9"
                     else:
                        message= "Aed.1.05"
                        
                    elif ((From in zone4) and (To in zone4)):
                     a=zone4.index(From)
                     b=zone4.index(To)
                     if (b==a+1 or a==b+1):
                        message= "Aed.0.9"
                     else:
                        message= "Aed.1.05"
                    
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
                            message= "price",":","Aed.2.05"
                     elif (r=="zone1" and s=="zone3"):
                            message= "price",":","Aed.2.9"
                     elif (r=="zone1" and s=="zone4"):
                            message= "price",":","Aed.2.9"
                     elif (r=="zone2" and s=="zone1"):
                            message= "price",":","Aed.2.05"

                     elif (r=="zone2" and s=="zone3"):
                            message= "price",":","Aed.2.05"
                     elif (r=="zone2" and s=="zone4"):
                            message= "price",":","Aed.2.9"
                     elif (r=="zone3" and s=="zone1"):
                            message= "price",":","Aed.2.9"
                     elif (r=="zone3" and s=="zone4"):
                            message= "price",":","Aed.2.05"
                            
                     elif (r=="zone3" and s=="zone2"):
                            message= "price",":","Aed.2.05"
                     elif (r=="zone4" and s=="zone1"):
                            message= "price",":","Aed.2.9"
                     elif (r=="zone4" and s=="zone2"):
                            message= "price",":","Aed.2.9"
                     elif (r=="zone4" and s=="zone3"):
                            message= "price",":","Aed.2.05"
                self.text.delete(0.0,END)
                self.text.insert(0.0,message)
                import datetime
                y=datetime.datetime.now()
                hour=y.hour
                minute=y.minute
                if (hour==23 and minute>28):
                    message1= "The next train will arrive at",5,":",45
                    
                if (From=="Dubai Healthcare City"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Oud Metha"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Jebel Ali"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Al Qusais-1"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Etisalat"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Al Karama"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Rashidiya "):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Burjuman"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Al Fahidi"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Al Ghubaiba"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break

                if (From=="Al Jaddaf"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Creek"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break

                if (From=="Airport Free Zone"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Al Jafiliya"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Emirates Towers"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Burj Khalifa / Dubai Mall"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Business Bay"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From==" Dubai International Financial Centre "):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Dubai World Trade Centre "):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Palm Deira"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
               

                if (From=="Airport Terminal-3"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="GGICO"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Abu Bakr Seddiq"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
              

                if (From=="Rashid Stadium"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break

                if (From=="Baniyas Square"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break

                if (From=="Airport Terminal-1"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break


                if (From=="Emirates"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break



                if (From=="Salahuddin"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                                

                if (From=="Deira City Centre"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break

                if (From=="Al Nahda"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Al Qiyadah"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Jebel Ali Industrial"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break

                if (From=="Noor Islamic Bank"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                  
                if (From=="Dubai Internet City"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Dubai Marina"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                   
                if (From=="Nakheel Harbor & Tower"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",47
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",47
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",55
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",03
                    elif(hour==6):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",7,":",07
                                break
                    elif(hour==7):
                        for minhand in range(7,60,8):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",8,":",03
                                break
                    elif(hour==8):
                        for minhand in range(3,60,8):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",9,":",07
                                break
                    elif(hour==9):
                        for minhand in range(7,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",10,":",01
                                break
                    elif(hour==10):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",11,":",01
                                break
                    elif(hour==11):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",12,":",01
                                break
                 
                    elif(hour==12):
                        for minhand in range(1,60,6):
                            if(minhand>=minute and minute<=55):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>55):
                                message1= "The next train will arrive at",13,":",01
                                break
                    elif(hour==13):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",14,":",05
                                break
                    elif(hour==14):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",15,":",01
                                break
                    elif(hour==15):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",16,":",05
                                break
                    elif(hour==16):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",17,":",05
                                break
                    elif(hour==17):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",18,":",05
                                break
                    elif(hour==18):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",19,":",05
                                break
                    elif(hour==19):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",20,":",05
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(5,60,6):
                            if(minhand>=minute and minute<=59):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>59):
                                message1= "The next train will arrive at",21,":",05
                                break
                    elif(hour==21):
                        for minhand in range(5,60,8):
                            if(minhand>=minute and minute<=53):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>53):
                                message1= "The next train will arrive at",22,":",01
                                break
                    elif(hour==22):
                        for minhand in range(1,60,8):
                            if(minhand>=minute and minute<=57):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>57):
                                message1= "The next train will arrive at",23,":",05
                                break
                    elif(hour==23):
                        for minhand in range(5,29,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="First Gulf Bank"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Energy"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Sharaf DG"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Al Rigga"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                
                if (From=="Al Ras"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Nakheel"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Abu Hail"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                    
                if (From=="Union  Square"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Ibn Battuta"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                if (From=="Jumeirah Lake Towers"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break
                if (From=="Mall of the Emirates"):
                    if (hour==0 or hour==1 or hour==2 or hour==3 or hour==4 or hour==5 or hour>23):
                        message1= "The next train will arrive at",5,":",45
                    if (hour==5):
                        if (minute>44):
                            message1= "The next train will arrive at",5,":",45
                        elif (minute>45):
                            message1= "The next train will arrive at",5,":",53
                        elif(minute>53):
                            message1= "The next train will arrive at",6,":",01
                    elif(hour==6):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",6,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",7,":",06
                                break
                    elif(hour==7):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",7,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",8,":",02
                                break
                    elif(hour==8):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",8,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",9,":",06
                                break
                    elif(hour==9):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",9,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",10,":",02
                                break
                    elif(hour==10):
                        for minhand in range(2,60,6):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",10,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",11,":",04
                                break
                    elif(hour==11):
                        for minhand in range(4,60,6):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",11,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",12,":",06
                                break
                 
                    elif(hour==12):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",12,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",13,":",02
                                break
                    elif(hour==13):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",13,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",14,":",06
                                break
                    elif(hour==14):
                        for minhand in range(6,60,8):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",14,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",15,":",02
                                break
                    elif(hour==15):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",15,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",16,":",06
                                break
                    elif(hour==16):
                        for minhand in range(6,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",16,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",17,":",00
                                break
                    elif(hour==17):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",17,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",18,":",00
                                break
                    elif(hour==18):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",18,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",19,":",00
                                break
                    elif(hour==19):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",19,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",20,":",00
                                break
                                
                                
                    elif(hour==20):
                        for minhand in range(0,60,6):
                            if(minhand>=minute and minute<=54):
                                message1= "The next train will arrive at",20,":",minhand
                                break
                            elif(minute>54):
                                message1= "The next train will arrive at",21,":",00
                                break
                    elif(hour==21):
                        for minhand in range(0,60,8):
                            if(minhand>=minute and minute<=56):
                                message1= "The next train will arrive at",21,":",minhand
                                break
                            elif(minute>56):
                                message1= "The next train will arrive at",22,":",02
                                break
                    elif(hour==22):
                        for minhand in range(2,60,8):
                            if(minhand>=minute and minute<=58):
                                message1= "The next train will arrive at",22,":",minhand
                                break
                            elif(minute>58):
                                message1= "The next train will arrive at",23,":",04
                                break
                    elif(hour==23):
                        for minhand in range(4,26,8):
                            if(minhand>=minute):
                                message1= "The next train will arrive at",23,":",minhand
                                break            
                            
                self.text2.delete(0.0,END)
                self.text2.insert(0.0,message1) 
                RedLine=["Rashidiya ","Emirates","Airport Terminal-3","Airport Terminal-1","GGICO","Deira City Centre","Al Rigga","Union  Square","Burjuman","Al Karama",
                "Al Jafiliya","Dubai World Trade Centre ","Emirates Towers"," Dubai International Financial Centre ","Burj Khalifa / Dubai Mall","Business Bay","Noor Islamic Bank",
                "First Gulf Bank","Mall of the Emirates","Sharaf DG","Dubai Internet City","Nakheel","Dubai Marina","Jumeirah Lake Towers","Nakheel Harbor & Tower",
                "Ibn Battuta","Energy","Jebel Ali Industrial","Jebel Ali"]
                GreenLine=["Etisalat","Al Qusais-1","Airport Free Zone","Al Nahda","Rashid Stadium","Al Qiyadah","Abu Bakr Seddiq","Abu Hail","Salahuddin","Union  Square","Baniyas Square",
                "Palm Deira","Al Ras","Al Ghubaiba","Al Fahidi","Burjuman","Oud Metha","Dubai Healthcare City","Al Jaddaf","Creek"]
                Via=["Union  Square","Burjuman"]
                message0= "THE NUMBER OF STATIONS AND INTERCHANGE STATION IS:"
                if((From in RedLine) and (To in RedLine) and (From!="Burjuman") and (From!="Union  Square") and (To!="Burjuman") and (To!="Union  Square")):
                    x=RedLine.index(From)
                    y=RedLine.index(To)
                    message2= From,"is",fabs(y-x),"stops from",To
                if((From in GreenLine) and (To in GreenLine) and (From!="Burjuman") and (From!="Union  Square") and (To!="Burjuman") and (To!="Union  Square")):
                    x=GreenLine.index(From)
                    y=GreenLine.index(To)
                    message2= From,"is",fabs(y-x),"stops from",To
                if((From in GreenLine) and (To in RedLine) and (From!="Burjuman") and (From!="Union  Square") and (To!="Burjuman") and (To!="Union  Square")):
                    x=GreenLine.index(From)
                    y=RedLine.index(To)
                    a=GreenLine.index("Union  Square")
                    b=GreenLine.index("Burjuman")
                    if((fabs(a-x))>(fabs(b-x))):
                        message= "Interchange Station is",GreenLine[b]
                        c=RedLine.index(GreenLine[b])
                        message2= From,"via",GreenLine[b],"to",To,"is",(fabs(b-x)+fabs(c-y)),"station(s)"
                    if((fabs(b-x))>(fabs(a-x))):
                        message2= "Interchange Station is",GreenLine[a]
                        c=RedLine.index(GreenLine[a])
                        message2= From,"via",GreenLine[a],"to",To,"is",(fabs(a-x)+fabs(c-y)),"station(s)"
                if((From in RedLine) and (To in GreenLine) and (From!="Burjuman") and (From!="Union  Square") and (To!="Burjuman") and (To!="Union  Square")):
                    x=RedLine.index(From)
                    y=GreenLine.index(To)
                    a=RedLine.index("Union  Square")
                    b=RedLine.index("Burjuman")
                    
                    if((fabs(a-x))>(fabs(b-x))):
                        message2= "Interchange Station is",RedLine[b]
                        c=GreenLine.index(RedLine[b])
                        message= From,"via",GreenLine[b],"to",To,"is",(fabs(b-x)+fabs(c-y)),"station(s)"
                    if((fabs(b-x))>(fabs(a-x))):
                        message2= "Interchange Station is",RedLine[a]
                        c=GreenLine.index(RedLine[a])
                        message2= From,"via",RedLine[a],"to",To,"is",(fabs(a-x)+fabs(c-y)),"station(s)"

                if(From=="Burjuman" and To=="Union  Square"):
                    message2= "Union  Square is 6 stops from Burjuman"
                if(From=="Union  Square" and To=="Burjuman"):
                    message2= "Burjuman is 6 stops from Union  Square"
                if(((From=="Burjuman") or (From=="Union  Square")) and (To!="Burjuman") and (To!="Union  Square") ):
                    if(To in GreenLine):
                        x=GreenLine.index(From)
                        y=GreenLine.index(To)
                        message2= From,"is",fabs(y-x),"stops from",To,"station(s)"
                    if(To in RedLine):
                        x=RedLine.index(From)
                        y=RedLine.index(To)
                        message2= From,"is",fabs(y-x),"stops from",To,"station(s)"
                if(((To=="Burjuman") or (To=="Union  Square")) and (From!="Burjuman") and (From!="Union  Square")):
                    if(From in GreenLine):
                        x=GreenLine.index(From)
                        y=GreenLine.index(To)
                        message2= From,"is",fabs(y-x),"stops from",To,"station(s)"
                    if(From in RedLine):
                        x=RedLine.index(From)
                        y=RedLine.index(To)
                        message2= From,"is",fabs(y-x),"stops from",To,"station(s)"
                self.text3.delete(0.0,END)        
                self.text3.insert(0.0,message2)
                
                
                
                
                      
                
                
                
                
                

            

            
            
       
root=Tk()
p = PhotoImage(file="C:\Users\Compaq\Desktop\pythonimg.gif")
l = Label(root, image=p)

l.pack_propagate(0)
l.pack()
l.grid()



root.option_add("*background","white")
root.configure(background='Blue')
root.title("Metro Planner")
root.geometry("480x455")
app=Application(root)
app.grid()
root.mainloop()

