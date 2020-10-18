sa1=input("Enter Sales 1 of Anil")
sa2=input("Enter Sales 2 of Anil")
sat=sa1+sa2
sr1=input("Enter Sales 1 of Raj")
sr2=input("Enter Sales 2 of Raj")
srt=sr1+sr2
sk1=input("Enter Sales 1 of Kumar")
sk2=input("Enter Sales 2 of Kumar")
skt=sk1+sk2
ss1=input("Enter Sales 1 of Sudha")
ss2=input("Enter Sales 2 of Sudha")
sst=ss1+ss2
n=[['Employees ','Sales1','Sales2','TotalSales'],['Anil      ',sa1+0.0,sa2+0.0,sat],['Raj       ',sr1+0.0,sr2+0.0,srt],['Kumar     ',sk1+0.0,sk2+0.0,skt],['Sudha     ',ss1+0.0,ss2+0.0,sst]]
for i in range(0,len(n)):
    for j in range(0,len(n[i])):
        print n[i][j],
    print 
