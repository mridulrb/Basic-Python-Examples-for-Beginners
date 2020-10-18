myfile=open("first.txt","r")
size=0
tsize=0
str1=" "
while str1:
    str1=myfile.readline()
    tsize=tsize+len(str1)
    size=size+len(str1.strip())
print "Size with all the characters",size
print "Total size of file",tsize
myfile.close()
