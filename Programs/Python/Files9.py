f1 = open("first.txt", "r")
f2 = open("Home.txt", "w")
old_text=raw_input("Enter text to be replaced")
new_text=''
for line in f1:
    f2.write(line.replace(old_text, new_text))
y = open("Home.txt","r")
f3=y.read()
for i in f3:
    print i,
f1.close()
f2.close()
y.close()
