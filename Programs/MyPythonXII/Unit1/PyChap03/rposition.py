# File name: ...\\MyPythonXII\Unit1\PyChap03\rposition.py
# Program to re-position all the elements of the array by shifting each of them
# one to one position before and by shifting the first element to the last position.
T = list() # Creating a default list/array

def Convert(T, Num):
    P = T[0]
    for i in range(0, Num):
        T[i] = T[i+1]
    T[Num-1] = P

Ch = 'Y'
i = N = 1
print ("Please enter values...")
while Ch == 'Y' or Ch == 'y'or Ch == 'Yes':
    print ("Enter number %d " % (i), end="")
    val = int(input())
    T.append(val)   # adding number into list
    print ("Do you want to add more...<y/n>: ", end="")
    Ch = input()
    if Ch == 'N' or Ch == 'n' or Ch == 'No' or Ch == 'NO':
        break
    else:
        N += 1

T.append(0)  # to avoid list index out of range in Convert function

ln= len(T)
if ln > 0:
    print("The content of initial array is:")
    for i in range(ln-1):
        print(T[i], end="   ")
    print()
    Convert(T, N)
    print("The content of changed array is:")
    for i in range(ln-1):
        print(T[i], end="   ")
