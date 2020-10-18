# File name: ...\\MyPythonXII\Unit2\PyChap02\Avlspace.py
class Directory:
    Freespace = Occupied = 0
    Docunames = []
    def Newdocuentry(self):
        print("Enter document names (<Enter>) to quit : ")
        nfile = " "
        ctr = 1
        while True:
            print("Enter name of document : ", ctr, end=" ")
            ndoc = input()
            if len(ndoc) > 0:
                self.Docunames.append(ndoc)
                ctr+=1
            else:
                break;
        self.Freespace = float(input("Enter free space : "))
        self.Occupied = float(input("Enter space occupied : "))         
    def RetFreespace(self):
        return (self.Freespace/1024)
    def Showfiles(self):
        print("Document names are : ")
        dlen = len(self.Docunames)
        for i in range(dlen):
            print (self.Docunames[i])
        print("Total free space available = ", self.RetFreespace())
                
Dr = Directory()
Dr.Newdocuentry()
Dr.Showfiles()
        			
