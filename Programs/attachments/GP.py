x=input("enter first term")
y=input("enter common ratio")
def gp(a,r):
    z=0
    for i in range(0,3):
        s=a*r**i
        z=z+s
    print z
gp(x,y)    
