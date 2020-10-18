n=input("Enter no of records:")
a=()
for i in range(n):
    b=()
    book_id=raw_input("Enter Book ID:")
    name=raw_input("Enter Book name:")
    book_type=raw_input("Enter Book type:")
    b+=(book_id,name,book_type)
    a+=((b),)
print a
for k in range(len(a)):
    if(a[k][2]=="Comedy"):
        print a[k]
