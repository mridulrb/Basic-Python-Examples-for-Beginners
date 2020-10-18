try:
    a=input("Enter a no")
    b=input("Enter a no")
    if (b==0):
        raise ZeroDivisionError,"Division not possible"
    print a/b
except ZeroDivisionError,e:
    print "Exception:",e.message
