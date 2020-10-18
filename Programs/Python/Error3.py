try:
    a=input("Enter a no")
    b=input("Enter a no")
    if(b==0):
        raise ZeroDivisionError,"Don't know"
    x=a/b
    print x
except ZeroDivisionError,g:
    print g.message
