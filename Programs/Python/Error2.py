for x in range(-2,3):
    print x,
    try:
        print 1/x
    except ZeroDivisionError,e:
        print e.message
    except:
        print "Exception Occured"
