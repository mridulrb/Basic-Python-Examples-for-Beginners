try:
    fs=open("/not there")
except IOError:
    print "file does not exist"
print "this line will always print"
