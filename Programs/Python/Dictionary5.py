n=input("Enter no of products")
products={}
for i in range (n):
    name=raw_input("Enter product name")
    price=raw_input("Enter product price")
    products[name]=price
print products
while 1:
    print "Select an option"
    print "1)Find the price"
    print "2)Exit"
    choice=int(raw_input("Enter choice"))
    if (choice==1):
        name=raw_input("Enter product name")
        for i in products:
            if(i==name):
                print products[name]
            else:
                print "Product does not exist"
    elif(choice==2):
        break
                   
    
