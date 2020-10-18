while(1):
    u=raw_input("choose any operation *,+,-,/")
    a=input("enter any no  ")
    b=input("enter any no 2  ")
    if u=="+":
        c=a+b
        print c
    elif u=="-":
        c=a-b
        print c
    elif u=="*":
        c=a*b
        print c
    elif u=="/":
        c=a/b
        print c
    else:
        print"chosse correct operator"
        
