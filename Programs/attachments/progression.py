x=input("enter no.")
n=input("enter the range of power")
def progression(a,y):
    z=0
    for i in range (1,y+1):
        m=a**i
        z=z+m
    print z+1
progression(x,n)
