# File name: ...\\MyPythonXII\Unit1\PyChap01\LabA_05.py
# Program to find volumes of geometrical shapes
import math
while (True):
    Volume = 0
    print()
    print (' M A I N   M E N U')
    print ('- - - - - - - - - -')
    print ("1. Volume of a Cube")
    print ("2. Volume of a Sphere")
    print ("3. Volume of a Pyramid")
    print ("4. Volume of a Cylinder")
    print ("5. Volume of a Triangular Prism")
    print ("6. Volume of a Cone")
    print ("7. Volume of a Cuboid")
    print ("8. Quit")
    print ('- - - - - - - - - -')
    		
    Opt = int(input( "Enter your option: "))
    if (Opt == 1) :
        s = float(input("Enter the side of the cube: "))
        Volume = s * s * s
        print("Volume of the cube is => %.2f" % Volume)
    elif (Opt == 2) :
        r = float(input("Enter the  radius of the sphere: "))
        Volume = 4/3 * (math.pi * math.pow(r, 3))
        print("Volume of the sphere is => %.2f" % Volume)
    elif (Opt == 3) :
        b = float(input("Enter the base of the pyramid: "))
        h = float(input("Enter the height of pyramid: "))
        Volume = 1/3 * b * h
        print("Volume of the pyramid is => %.2f" % Volume)
    elif (Opt == 4) :
        r = float(input("Enter the radius of cylinder: "))
        h = float(input("Enter the height of cylinder: "))
        Volume = math.pi * math.pow(r, 2) * h
        print("Volume of the cylinder is => %.2f" % Volume)
    elif (Opt == 5) :
        a = float(input("Enter the area of triangular prism: "))
        h = float(input("Enter the height of triangular prism: "))
        Volume = a * h
        print("Volume of the triangular prism is => %.2f" % Volume)
    elif (Opt == 6) :
        r = float(input("Enter radius of the cone: "))
        h = float(input("Enter height of the cone: "))        
        Volume = 1/3 * (math.pi * math.pow(r, 2) * h)
        print("Volume of the cone is => %.2f" % Volume)
    elif (Opt == 7) :
        l = float(input("Enter length of the cuboid: "))
        b = float(input("Enter breadth of the cuboid: "))
        h = float(input("Enter height of the cuboid: "))        
        Volume = l * b * h
        print("Volume of the cuboid is => %.2f" % Volume)
    elif (Opt == 8):
        break;
    x = input("Press <Enter> to continue...")
    
