while(1):
     n=input("enter number")
     Num = n
     Sum=0
     m = n%10
     n=n/10
     y=n%10
     n=n/10
     while (n!=0):
              Sum = Sum + pow(m,3)+pow(y,3)+pow(n,3)
              if (Sum == Num):
                  print "yes"
                  break
              else:
                  print "no"
                  break
