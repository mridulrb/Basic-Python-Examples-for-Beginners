line=raw_input("Enter line:")
sub=raw_input("Enter substring:")
lenline=len(line)
lensub=len(sub)
start=count=0
end=lenline
while True:
    pos=line.find(sub,start,end)
    if (pos != -1):
        count += 1
        start=pos+lensub
    else:
        break
    if(start>=lenline):
        break
print "No. of occurrences of",sub,":",count
