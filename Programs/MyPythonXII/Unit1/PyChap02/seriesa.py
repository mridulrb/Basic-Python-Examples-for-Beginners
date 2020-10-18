# File name: ...\\MyPythonXII\Unit1\PyChap02\seriesa.py
# File name: ...\MyPython\Unit3\PyChap06\SeriesA.py
# Function to find sequence sum
def seqsum( x, n):
    sum, div, fact = 1, 2, 1
    num = x
    for i in range (2, n+1):
        num = num*n
        fact = fact*(div)*(div-1)
        term = (num/fact)
        div = div+2
        sum = sum + term
    return sum
				
def main():
    c=seqsum(5,4)
    print("The sum of sequence is: %.2f" % c)
main()
