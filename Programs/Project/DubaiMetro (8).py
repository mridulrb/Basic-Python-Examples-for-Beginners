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
                          "Burj Khalifa / Dubai Mall","Dubai International Financial Centre ","Emirates Towers","Dubai World Trade Centre ","Al Jafiliya","Al Karama",
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
        self.text4=Text(self,width=50,height=10,wrap=WORD)
        self.text4.grid(row=9,column=0,columnspan=4,sticky=W)
        
        
        



        

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
            zone3=["Business Bay","Burj Khalifa / Dubai Mall","Dubai International Financial Centre ","Emirates Towers","Dubai World Trade Centre ","Al Jafiliya","Al Karama","Creek","Al Jaddaf","Dubai Healthcare City","Oud Metha","Burjuman","Al Fahidi","Al Ghubaiba"]
            zone4=["Al Ras","Baniyas Square","Palm Deira","Union  Square","Al Rigga","Deira City Centre","GGICO","Airport Terminal-1","Airport Terminal-3","Emirates","Rashidiya ","Salahuddin","Abu Bakr Seddiq","Abu Hail",
            "Al Qiyadah","Rashid Stadium","Al Nahda","Airport Free Zone","Al Qusais-1","Etisalat"]
            liststations=["Jebel Ali","Jebel Ali Industrial","Noor Islamic Bank","First Gulf Bank",
                          "Mall of the Emirates","Sharaf DG","Dubai Internet City","Nakheel","Dubai Marina","Jumeirah Lake Towers",
                          "Nakheel Harbor & Tower","Ibn Battuta","Energy","Business Bay",
                          "Burj Khalifa / Dubai Mall","Dubai International Financial Centre ","Emirates Towers","Dubai World Trade Centre ","Al Jafiliya","Al Karama",
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
                if (From=="Dubai International Financial Centre "):
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
                            
                self.text2.delete(0.0,END)
                self.text2.insert(0.0,message1) 
                RedLine=["Rashidiya ","Emirates","Airport Terminal-3","Airport Terminal-1","GGICO","Deira City Centre","Al Rigga","Union  Square","Burjuman","Al Karama",
                "Al Jafiliya","Dubai World Trade Centre ","Emirates Towers","Dubai International Financial Centre ","Burj Khalifa / Dubai Mall","Business Bay","Noor Islamic Bank",
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
                        message2= From,"via",GreenLine[b],"to",To,"is",(fabs(b-x)+fabs(c-y))
                    if((fabs(b-x))>(fabs(a-x))):
                        message2= "Interchange Station is",GreenLine[a]
                        c=RedLine.index(GreenLine[a])
                        message2= From,"via",GreenLine[a],"to",To,"is",(fabs(a-x)+fabs(c-y))
                if((From in RedLine) and (To in GreenLine) and (From!="Burjuman") and (From!="Union  Square") and (To!="Burjuman") and (To!="Union  Square")):
                    x=RedLine.index(From)
                    y=GreenLine.index(To)
                    a=RedLine.index("Union  Square")
                    b=RedLine.index("Burjuman")
                    
                    if((fabs(a-x))>(fabs(b-x))):
                        message2= "Interchange Station is",RedLine[b]
                        c=GreenLine.index(RedLine[b])
                        message= From,"via",GreenLine[b],"to",To,"is",(fabs(b-x)+fabs(c-y))
                    if((fabs(b-x))>(fabs(a-x))):
                        message2= "Interchange Station is",RedLine[a]
                        c=GreenLine.index(RedLine[a])
                        message2= From,"via",RedLine[a],"to",To,"is",(fabs(a-x)+fabs(c-y))

                if(From=="Burjuman" and To=="Union  Square"):
                    message2= "Union  Square is 6 stops from Burjuman"
                if(From=="Union  Square" and To=="Burjuman"):
                    message2= "Burjuman is 6 stops from Union  Square"
                if(((From=="Burjuman") or (From=="Union  Square")) and (To!="Burjuman") and (To!="Union  Square") ):
                    if(To in GreenLine):
                        x=GreenLine.index(From)
                        y=GreenLine.index(To)
                        message2= From,"is",fabs(y-x),"stops from",To
                    if(To in RedLine):
                        x=RedLine.index(From)
                        y=RedLine.index(To)
                        message2= From,"is",fabs(y-x),"stops from",To
                if(((To=="Burjuman") or (To=="Union  Square")) and (From!="Burjuman") and (From!="Union  Square")):
                    if(From in GreenLine):
                        x=GreenLine.index(From)
                        y=GreenLine.index(To)
                        message2= From,"is",fabs(y-x),"stops from",To
                    if(From in RedLine):
                        x=RedLine.index(From)
                        y=RedLine.index(To)
                        message2= From,"is",fabs(y-x),"stops from",To
                self.text3.delete(0.0,END)        
                self.text3.insert(0.0,message2)
                if (To=="Dubai Healthcare City"):
                    message3= ["The feeder buses available are:","22-Healthcare city-Al Nahda 1","42-GHUBAIBA BUS STATION :Al Ghubaiba 1"," C7-HOR AL ANZ BUS STATION-HEALTHCARE CITY"]
                if(To=="Emirates"):
                     message3= ["The feeder buses available are:","F8-Al Nahda 2-Mamzar ,Century Mall"]
                if(To=="Airport Terminal-3"):
                     message3= ["The feeder buses available are:","C1-Satwa Bus Station","88-Nakheel MS"]
                if(To=="Airport Terminal-1"):
                     message3= ["The feeder buses available are:","C1-Satwa Bus Station","4-Gold Souq Bus Station-Rashidiya MS","11A-Gold souq Bus Station-Al Awir Terminus","32C-Al Qusais-1 Bus Station-Satwa Bus Station","33-Ghubaiba Bus Station-Al Qusais-1 Bus Station","42-Ghubaiba Bus Station-Airport Airport Terminal-1","48-Mamzar","Century Mall-Rashidiya  MS","64A-Glod Souk Bus Station-Ras Al Khor","88-Airport Airport Terminal-3-Nakheel MS"]
                if(To=="GGICO"):
                     message3= ["The feeder buses available are:","42-Ghubaiba Bus Station-airport Airport Terminal-1"]
                if(To=="Deira City Centre"):
                     message3= ["The feeder buses available are:","C10-Hamriya Port- Jumeirah Beach Park","C14-Mamzar","Century Mall-Safa Terminus","C15-Hamriya Port-Al Wasl Park Terminus","C19-Ghubaiba Bus Station-Al Qusais-1 Industrial Area","X28-Lulu Village-Nakheel MS","22-Health Care City-Al Nahda 1 ","27-Gold Souq Bus Station-Dubai Mall","33-Ghubaiba Bus Station-Al Qusais-1 Bus Station","53-Ghubaiba Bus Station-International City","88-Airport Airport Terminal-3-Nakhell MS"]
                if(To=="Al Rigga"):
                     message3= ["The feeder buses available are:","C9-Satwa Bus Station-Hor Al Anz East"]
                if(To=="Union Square"):
                     message3= ["The feeder buses available are:","C1-Airport Airport Terminal-3-Satwa Bus Station","C2-Zabeel Park-Airport Terminal 2","C4-Gold Souq Bus Station-Jadaf","C5-Gold Souq bus Station-Ghubaiab Bus Satation","C7-Hor Al Anz Bus Station-Healthcare City","C9-Satwa Bus Station-Hor Al Anz East ","C28-Gold Souq Bus Station-Mamzar Beach Park","C55-Gold Souq Bus Station-Ghubaiba Bus Station","E303-Union Square Square MS-Sharjah","E700-Fujairah-Union Square Square MS","E400-Union Square Square MS-Ajman","X94-Gold Souq Bus Station-Dubai Investment Park","4-Gold Souq Bus Station-Rashidiya  MS","11A-Gold Souq Bus Station-Al Awir Terminus","27-Gold Souq Bus Station-Dubai Mall","64A-Gold Souq Bus Station-Ras Al Khor"]
                if(To=="Burjuman"):
                     message3= ["The feeder buses available are:","C2-Zabeel Park-Airport Terminal 2","C3-Hor Al Anz Bus Station-Karama Bus Station","C5-Gold Souq Bus Station-Ghubaiba Bus Station","C10-Hamriya Port-Jumeirah Beach Park","C18-Shaikh Rashid Colony","AlQusais-Lamcy Plaza    ","C19-Ghubaiba Bus Station-Al Qusais-1 Industrial Area","C55-Gold Souq Bus Station-Ghubaiba Bus Station","X23-Gold Souq Bus Station–International City","21-Ghubaiba Bus Station–Al Quoz Ind. Area 4","33-Ghubaiba Bus Station–Al Qusais-1 Bus Station","42-Ghubaiba Bus Station–Airport Airport Terminal-1","44-Ghubaiba Bus Station–Dubai Festival City","61-Ghubaiba Bus Station–Ras Al Khor","61D-Ghubaiba Bus Station–Nad Al Sheba Clinic ","66-Ghubaiba Bus Station–Faqa Terminus","67-Ghubaiba Bus Station–Endurance City Terminus","91-Ghubaiba Bus Station–Jebel Ali Bus Station"]
                if(To=="Al Karama"):
                     message3= ["The feeder buses available are:","C2-Airport Terminal 2–Zabeel Park","C10-Hamriya Port–Jumeirah Beach Park","C15 Hamriya Port–Al Wasl Park","C26-Al Wasl Park–Al Qusais-1 Industrial Area","21-Ghubaiba Bus Station–Al Quoz Ind. Area 4","61-Ghubaiba Bus Station–Ras Al Khor Industrial Area","88-Airport Airport Terminal-3–Nakheel MS"]
                if(To=="Al Jafiliya"):
                     message3= ["The feeder buses available are:","C2-Zabeel Park–Airport Terminal 2","C15-Hamriya Port–Al Wasl Park Terminus","C26-Al Wasl Park Terminus–Al Qusais-1 Industrial Area","X10-Gold Souq Bus Station–Al Quoz Bus Station","X28-Lulu Village–Nakheel MS","X92-Ghubaiba Bus Station–Dubai Investment Park","10-Gold Souq Bus Station–Al Quoz Bus Station ","21-Ghubaiba Bus Station–Al Quoz Ind. Area 4","27-Gold Souq Bus Station-Dubai Mall","61-Ghubaiba Bus Station–Ras Al Khor Ind. Area","88-Airport Airport Terminal-3–Nakheel MS"]
                if(To=="Dubai World Trade Centre "):
                     message3= ["The feeder buses available are:","F11-Financial Centre MS–Satwa","21-Ghubaiba Bus Station–Al Quoz Ind. Area 4","98E-Satwa Bus Station–Al Quoz Ind. Area 3"]
                if(To=="Emirates Towers"):
                     message3= ["The feeder buses available are:","F11 Financial Centre MS – Satwa","21-Ghubaiba Bus Station–Al Quoz Ind. Area 4","27-Gold Souq Bus Station–Dubai Mall","98E-Satwa Bus Station–Al Quoz Ind. Area 3"]
                if(To=="Dubai International Financial Centre "):
                     message3= ["The feeder buses available are:","F11-Financial Centre MS–Satwa"] 
                if(To=="Burj Khalifa / Dubai Mall"):
                     message3= ["The feeder buses available are:","F13-Burj Khalifa/Dubai Mall MS–Dubai Mall","F16-Burj Khalifa/Dubai Mall MS–Jumeirah 2"]
                if(To=="Business Bay"):
                     message3= ["The feeder buses available are:","F16 Dubai Mall – Jumeirah 2","F20 Business Bay MS – Al Safa 1","7-Ghubaiba Bus Station–Iranian Clinic Al Quoz"]
                if(To=="Noor Islamic Bank"):
                     message3= ["The feeder buses available are:","F15-Noor Islamic Bank MS–Al Quoz Ind. Area 2 ","21-Ghubaiba Bus Station–Al Quoz Ind. Area 4"]
                if(To=="First Gulf Bank"):
                     message3= ["The feeder buses available are:","F25-First Gulf Bank MS land side–Al Quoz 3 & 4","12-Ghubaiba Bus Station–Al Quoz Bus Station"]
                if(To=="Mall of the Emirates"):
                     message3= ["The feeder buses available are:","F30-Mall of the Emirates MS–Arabian Ranches","F33-Mall of the Emirates MS–Al Barsha 3","93-Ghubaiba Bus Station–The Greens"]
                if(To=="Dubai Internet City"):
                     message3= ["The feeder buses available are:","F31-The Meadows–Dubai Internet City MS","88-Airport Airport Terminal-3–Nakheel MS","X28-Lulu Village–Nakheel MS"] 
                if(To=="Nakheel"):
                     message3= ["The feeder buses avaliable are:","X28-Lulu Village-Nakheel MS","88-Airport Airport Terminal-3–Nakheel MS"]
                if(To=="Dubai Marina"):
                     message3= ["The feeder buses avaliable are:","F37-Marina MS–Dubai Marina"]
                if(To=="Jumeirah Lake Towers"):
                     message3= ["The feeder buses available are:","F37-Marina MS–Jumeirah Lakes Tower MS–Dubai Marina"]
                if(To=="Ibn Battuta"):
                     message3= ["The feeder buses avaliable are:","E101-Abu Dhabi–Ibn Batutta","F43-Ibn Battuta MS–Discovery Gardens","F44-Ibn Battuta MS–The Gardens","F46-Ibn Battuta MS–IMP Zone","F48-Ibn Battuta MS–Dubai Investment Park","F53-Ibn Battuta MS–Dubai Industrial City","8-Ibn Battuta MS–Gold Souk Bus Station"]
                if(To=="Jebel Ali"):
                     message3= ["The feeder buses avaliable are:","F54-Jafza South–Jebel Ali MS","99-New East Camp–Marine Control Towers"]
                if(To=="Jebel Ali Industrial"):
                     message3= ["The feeder buses avaliable are:","F54-Jafza South–Jebel Ali MS","99-New East Camp–Marine Control Towers"]
                    

                    
                if(To=="Etisalat"):
                     message3= ["The feeder buses avaliable are:","31-Gold Souq Bus Station–Oud Al Mateena"]
                if(To=="Al Qusais-1"):
                     message3= ["The feeder buses avaliable are:","13 Gold Souq Bus Station – Al Qusais-1 Bus Station","31-Gold Souq Bus Station–Oud Al Mateena","64-Gold Souq Bus Station–Ras Al Khor"]
                if(To=="Airport Free Zone"):
                     message3= ["The feeder buses avaliable are:","13-Gold Souq Bus Station–Al Qusais-1 Bus Station","17-Al Sabkha Bus Station–Al Qusais-1 Bus Station ","31-Gold Souq Bus Station–Oud Al Mateena","64-Gold Souq Bus Station–Ras Al Khor","C18-Shaikh Rashid Colony"," Al Qusais-1–Lamcy Plaza ","C19-Ghubaiba Bus Station–Al Qusais-1 Industrial Area","x28-Lulu Village–Nakheel MS"]
                if(To=="Al Nahda"):
                     message3= ["The feeder buses avaliable are:","13 Gold Souq Bus Station–Al Qusais-1 Bus Station","13A Gold Souq Bus Station–Al Qusais-1 Bus Station","17 Al Sabkha Bus Station–Al Qusais-1 Bus Station","22 Healthcare City–Al Nahda 1","31 Gold Souq Bus Station–Oud Al Mateena","64 Gold Souq Bus Station–Ras Al Khor","C18 Shaikh Rashid Colony"," Al Qusais-1–Lamcy Plaza","C19 Ghubaiba Bus Station–Al Qusais-1 Industrial Area","X28 Lulu Village–Nakheel MS"]
                if(To=="Rashid Stadium"):
                     message3= ["The feeder buses available are:","13-Gold Souq Bus Station–Al Qusais-1 Bus Station","13A Gold Souq Bus Station–Al Qusais-1 Bus Station","17 Al Sabkha Bus Station–Al Qusais-1 Bus Station","22 Healthcare City–Al Nahda 1","64 Gold Souq Bus Station–Ras Al Khor","C18 Shaikh Rashid Colony"," Al Qusais-1–Lamcy Plaza","C19 Ghubaiba Bus Station–Al Qusais-1 Industrial Area","X28 Lulu Village–Nakheel MS"]
                if(To=="Al Qiyadah"):
                     message3= ["The feeder buses available are:","C9-Al Satwa Bus Station–Hor Al Anz East"]
                if(To=="Abu Hail"):
                     message3= ["The feeder buses available are:","13 Gold Souq Bus Station–Al Qusais-1 Bus Station","13A Gold Souq Bus Station–Al Qusais-1 Bus Station","48 Mamzar"," Century Mall–Al Rashidiya  MS","C2 Zabeel Park–Airport Terminal 2","C3 Hor Al Anz Bus Station–Karama Bus Station","C7 Hor Al Anz Bus Station–Healthcare City","C9 Satwa Bus Station–Hor Al Anz East","C19 Ghubaiba Bus Station–Al Qusais-1 Industrial Area","X28 Lulu Village–Nakheel MS"]
                if(To=="Abu Bakr Seddiq"):
                     message3= ["The feeder buses available are:","13 Gold Souq Bus Station–Al Qusais-1 Bus Station","13A Gold Souq Bus Station–Al Qusais-1 Bus Station","48 Mamzar"," Century Mall–Al Rashidiya  MS","C2 Zabeel Park–Airport Terminal 2","C19 Ghubaiba Bus Station–Al Qusais-1 Industrial Area","x28 Lulu Village–Nakheel MS"] 
                if(To=="Salahuddin"):
                     message3= ["The feeder buses available are:","10-Gold Souq Bus Station–Al Quoz Bus Station","13-Gold Souq Bus Station–Al Qusais-1 Bus Station","13A-Gold Souq Bus Station–Al Qusais-1 Bus Station","C2-Zabeel Park–Airport Terminal 2","C28-Gold Souq Bus Station–Mamzar Beach Park"]
                
                if(To=="Baniyas Square"):
                     message3= ["The feeder buses available are:","17-Al Sabkha Bus Station–Al Qusais-1 Bus Station","64A-Gold Souq Bus Station–Ras Al Khor"]
                if(To=="Palm Deira"):
                     message3= ["The feeder buses available are:","8-Gold Souq Bus Station–Al Mina Al Siyahi","C1-Airport Airport Terminal-3–Satwa Bus Station","C2-Zabeel Park–Airport Terminal 2","C3-Hor Al Anz Bus Station-Karama Bus Station","C7-Hor Al Anz Bus Station–Healthcare City","C9-Satwa Bus Station–Hor Al Anz East","C18-Shaikh Rashid Colony"," Al Qusais-1–Lamcy Plaza","C55-Gold Souq Bus Station–Ghubaiba Bus Station","X10-Gold Souq Bus Station–Al Qouz Bus Station","X13-LuLu Village–Al Satwa Bus Station","X23-Gold Souq Bus Station–International City"]
                if(To=="Al Ras"):
                     message3= ["The feeder buses available are:","27-Gold Souq Bus Station–Dubai Mall","53-Ghubaiba Bus Station–International City","C2-Zabeel Park–Airport Terminal 2","C4-Gold Souq Bus Station–Jadaf","C7-Hor Al Anz Bus Station–Healthcare City","C9-Satwa Bus Station–Hor Al Anz East","C28-Gold Souq Bus Station–Mamzar Beach Park","C55-Gold Souq Bus Station–Ghubaiba Bus Station"]
                if(To=="Al Ghubaiba"):
                     message3= ["The feeder buses available are:","8-Gold Souq Bus Station–Al Mina Al Siyahi","C5-Gold Souq Bus Station–Ghubaiba Bus Station","C7-Hor Al Anz Bus Station–Healthcare City","C9-Satwa Bus Station–Hor Al Anz East","X13-LuLu Village–Al Satwa Bus Station"]    
                if(To=="Al Fahidi"):
                     message3= ["The feeder buses available are:","21-Ghubaiba Bus Station–Al Quoz Ind. Area 4","33-Ghubaiba Bus Station–Qusais Bus Station","42-Ghubaiba Bus Station–Airport Airport Terminal-1 ","44-Ghubaiba Bus Station–Dubai Festival City","61-Ghubaiba Bus Station–Ras Al Khor","61D-Ghubaiba Bus Station-Nad Al Sheba Clinic","66-Ghubaiba Bus Station–Faqa Terminus","67-Ghubaiba Bus Station–Endurance City Terminus","91-Ghubaiba Bus Station–Jebel Ali Bus Station","C1-Airport Airport Terminal-3–Satwa Bus Station","C2-Zabeel Park–Airport Terminal 2","C3-Hor Al Anz Bus Station–Karama Bus Station","C5-Gold Souq Bus Station–Ghubaiba Bus Station","C7-Hor Al Anz Bus Station–Healthcare City","C18-Shaikh Rashid Colony,Al Qusais-1–Lamcy Plaza","C19-Ghubaiba Bus Station-Al Qusais-1 Industrial Area","C55-Gold Souq Bus Station-Ghubaiba Bus Station","X23-Gold Souq Bus Station–International City"]
                if(To=="Oud Metha"):
                     message3= ["The feeder buses available are:","22-Healthcare City – Al Nahda 1","42-Ghubaiba Bus Station-Airport Airport Terminal-1","44-Ghubaiba Bus Station-Dubai Festival City","61D-Ghubaiba Bus Station-Nad Al Sheba Clinic","66-Ghubaiba Bus Station-Faqa Terminus","67-Ghubaiba Bus Station-Endurance City Terminus","C4-Gold Souq Bus Station-Jadaf","C7-Hor Al Anz Bus Station-Healthcare City","C18-Shaikh Rashid Colony"," Al Qusais-1-Lamcy Plaza","X23-Gold Souq Bus Station–International City"]
                self.text4.delete(0.0,END)        
                self.text4.insert(0.0,message3)
                

            
 
            
            
       
root=Tk()
p = PhotoImage(file="C:\Users\Rajesh.GCP\Desktop\pythonimg.gif")
l = Label(root, image=p)

l.pack_propagate(0)
l.pack()
l.grid()



root.option_add("*background","white")
root.configure(background='Blue')
root.title("Metro Planner")
root.geometry("580x611")
app=Application(root)
app.grid()
root.mainloop()




            
