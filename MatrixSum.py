x=[input("Enter the first nested list ")]
y=[input("Enter the second nested list ")]
for i in range (0,len(x)):
  for j in range(0,len(x[i])):
    x[i][j]+=y[i][j]
for i in range(0,len(x)):
  for j in range(0,len(x[i])):
    print (x[i][j]),
  print

