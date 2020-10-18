# File name: ...\\MyPythonXII\Unit1\PyChap02\listmerge.py
# User-defined function to merge three different lists into a single tuple. 
def merge(*lists):
    newlist = lists[:]
    for x in lists:
        if x not in newlist:
            newlist.extend(x)
    return newlist

List1 = [87, 78, 88, 86, 69]
List2 = [65, 66, 58, 66, 77]
List3 = [56, 86, 67, 82, 87]
print(merge(List1, List2, List1))
