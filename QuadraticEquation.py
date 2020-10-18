def quadroots(a,b,c):
    import math
    D=(b**2)-4*(a)*(c)
    root1=(-1*b+math.sqrt(D))/2*a
    root2=(-1*b-math.sqrt(D))/2*a
    return root1,root2
x=input("Enter the coefficient of x^2:")
y=input("Enter the coefficient of x:")
z=input("Enter the constant:")
print ('The roots are',quadroots(x,y,z)) 

