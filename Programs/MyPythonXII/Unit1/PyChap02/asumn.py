# File name: ...\\MyPythonXII\Unit1\PyChap02\asumn.py
# Function to find the sum of series (1) + (1+2) + (1+2+3) + ......+ (1+2+3+...+N)
def sumseries(n):
    sum = 0
    sum1 = 0
    for i in range(1,n+1):
        sum = 0
        for j in range(1,i+1):
            sum = sum + j
        sum1 = sum1 + sum
    return(sum1)
		
def main():
    N = int(input("Enter the value of N: "))
    sum = sumseries(N)
    print("The sum of N series is: ", sum)
main()
