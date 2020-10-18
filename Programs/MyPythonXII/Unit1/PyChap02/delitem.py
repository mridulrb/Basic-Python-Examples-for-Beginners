# File name: ...\\MyPythonXII\Unit1\PyChap02\delitem.py
# Deleting even numbers from a numeric list
Num = [23, 54, 32, 34, 44, 33, 35, 66, 27, 88, 69, 54]
ln = len(Num)
ctr = 0
print ("The original list is: ", Num)
while ctr < ln:
    if Num[ctr] % 2 == 0:   # check the list value is even or not
        del Num[ctr]
        ln-=1 # when an element is deleted the length should be -1, i.e., ln =  ln - 1
        ctr-=1 # the counter should decrease by 1 because, every time 
                # when if statement is finished the counter increases its value
                # so, for consecutive even value it is necessary to decrease
                # the counter value, i.e., ctr = ctr - 1
    ctr+=1    
        
print ("The new list after deleting even elements: ", Num)
