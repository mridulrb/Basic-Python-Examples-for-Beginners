n=list(input("Enter the nested list: "))
for i in range(0,len(n)):
  for j in range(0,len(n[i])):
    print (n[i][j]),
  print
for i in range(0,len(n)):
  print ("Sum of row",i+1,"is",sum(n[i]))
for j in range (0,len(n)):
  s=0
  for k in range(0,len(n[i])):
    s+=n[k][j]
  print ("Sum of column",j+1,"is",s)

