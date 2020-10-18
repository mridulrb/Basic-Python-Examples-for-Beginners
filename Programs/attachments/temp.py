while(1):
    print"choose the option you want"
    print"A)Celsius to Farenheit"
    print"B)Farenheit to Celsius"
    choice=raw_input("choose A or B  ")
    if choice=="A":
        C=input("Enter any temperature in Celcius ")
        T=((1.8*C)+32)
        print str(T)+"F"
    elif choice=="B":
        F=input("Enter any temperature in Farenheit  ")
        T=(0.556*(F-32))
        print str(T)+"C"
    else:
        print"choose correct option"
    
    
