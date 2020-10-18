#predict the output for these calls
"""
1.divide(2,1)
2.divide(2,0)
3.divide("2","1")
"""
def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print "Division by Zero"
    else:
        print "The result is",result
    finally:
        print "Executing the finally clause"
