# File name: ...\\MyPythonXII\Unit1\PyChap01\area1.py
# Program find to area and perimeter of a rectangle with return values

def rectangle(length, breadth):
    area = length * breadth # Area of rectangle
    perimeter = 2 * ( length + breadth ) # Perimeter of rectangle
    return area, perimeter # Returning more than one value
    
def main():
    l = float(input("Enter length of rectangle: "))
    b = float(input("Enter breadth of rectangle: "))
    a, p = rectangle(l, b)  # Returned values
    print ("Area is: %0.2f" % a)
    print ("Perimeter is: %0.2f" % p)
main()
