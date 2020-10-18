class library:
    def __init__(self):
        self.bookno=0
        self.bookname="abc"
        self.publisher="xyz"
        self.price=0
        self.noofcopies=0
        self.noofcopiesissued=0    
    def putdata(self):
        self.bookno=input("Enter Book no.:")
        self.bookname=raw_input("Enter Book name:")
        self.publisher=raw_input("Enter Publisher:")
        self.price=input("Enter Book price:")
        self.noofcopies=input("Enter no of copies:")
        self.copiesissued=input("Enter no of copies issued:")
    def issue(self,a):
        if(self.bookno==a):
            if((self.noofcopies-self.copiesissued)>0):
                self.copiesissued-=1
            else:
                print "Book not in Stock!"
        else:
            print "Book not Available!"
    def returnbook(self,a):
        if(self.bookno==a):
            self.copiesissued+=1
    def display(self,a):
        if(self.bookno==a):
            print "Book no.:",self.bookno
            print "Book name:",self.bookname
            print "Publisher:",self.publisher
            print "No of copies:",self.noofcopies
            print "Copies issued:",self.copiesissued

m=[]
l=library()
while True:
    print "    1)Create"
    print "    2)Issue"
    print "    3)Return"
    print "    4)Display"
    print "    5)Exit"
    choice=input("Enter choice:")
    if(choice==1):
        r=[]
        n=input("Enter no of records:")
        for i in range(n):
            l.putdata()
            r+=[l]
        m+=[r]
    elif(choice==2):
        no=input("Enter Book no.:")
        l.issue(no)
    elif(choice==3):
        no=input("Enter Book no.")
        l.returnbook(no)
    elif(choice==4):
        no=input("Enter Book no.:")
        l.display(no)
    elif(choice==5):
        break
    else:
        print "Invalid Choice!"
