class Bank:
    b=[]
    def __init__(self):
        self.acc_no=0
        self.acc_name=""
        self.amount=0
    def putdata(self):
        self.acc_no=input("Enter Account no.:")
        self.acc_name=raw_input("Enter Account name:")
        self.amount=input("Enter Amount:")
        l=[self.acc_no,self.acc_name,self.amount]
        Bank.b.append(l)
    def disp(self,accno):
        y=0
        for i in range(len(Bank.b)):
            if(Bank.b[i][0]==accno):
                print "Account Number:",Bank.b[i][0]
                print "Account Name:",Bank.b[i][1]
                print "Account Amount:",Bank.b[i][2]
                y+=1
        if(y==0):
            print "Record not found!"
    def Withdraw(self,accno):
        y=0
        withdrawamt=input("Enter Amount to be withdrawn:")
        for i in range(len(Bank.b)):
            if(Bank.b[i][0]==accno):
                Bank.b[i][2]-=withdrawamt
                y+=1
        if(y==0):
            print "Record not found!"
    def Deposit(self,accno):
        y=0
        depositamt=input("Enter Amount to be deposited:")
        for i in range(len(Bank.b)):
            if(Bank.b[i][0]==accno):
                Bank.b[i][2]+=depositamt
                y+=1
        if(y==0):
            print "Record not found!"
    
s=Bank()
while True:
    print "   1)Create"
    print "   2)Display"
    print "   3)Withdraw"
    print "   4)Deposit"
    print "   5)Exit"
    choice=input("Enter choice:")
    if(choice==1):
        s.putdata()
    elif(choice==2):
        bankaccno=input("Enter Account no.:")
        s.disp(bankaccno)
    elif(choice==3):
        bankaccno=input("Enter Account no.:")
        s.Withdraw(bankaccno)
    elif(choice==4):
        bankaccno=input("Enter Account no.:")
        s.Deposit(bankaccno)
    elif(choice==5):
        break
    else:
        print "Invalid Choice!"
