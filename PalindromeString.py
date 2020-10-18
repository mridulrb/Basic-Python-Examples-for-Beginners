def stringpalindrome(x):
    s=''
    for i in range(len(x)-1,-1,-1):
        s=s+x[i]
    if (s==x and (len(x)%2==1)):
        print ("It is a palindrome")
    else:
        print ("It is not a palindrome")
x=raw_input("Enter the word")
stringpalindrome(x)

