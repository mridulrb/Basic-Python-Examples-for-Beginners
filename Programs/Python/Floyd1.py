employees={"125691":"Ram","29845":"Shyam"}
find=raw_input("Enter employee id")
for key in employees:
        if(key==find):
                print "found"
                print key,employees[key]
        break
else:
        print "Not found"
