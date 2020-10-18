fn=raw_input("Enter file name")
if fn!=" ":
    f=open(fn,'r')
else:
    print "Does not exist"
"""try:
    f=open(fn,'r')
except IOError:
    print "file does not exist"
"""
