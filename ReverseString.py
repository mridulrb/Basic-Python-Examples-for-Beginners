def reverse(x):
    s=''
    for i in range(len(x)-1,-1,-1):
        s=s+x[i]
    return s
x=raw_input("Enter the word")
print (reverse(x))

        

