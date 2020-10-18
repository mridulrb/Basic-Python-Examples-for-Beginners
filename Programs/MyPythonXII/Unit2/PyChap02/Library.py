# File name: ...\\MyPythonXII\Unit2\PyChap02\Library.py
class Library:
    def ReadBooks(self):
        print ("Enter book details...")
        self.Name = input("Enter name: ")
        self.English_books = int(input("Enter total english books: "))
        self.Hindi_books = int(input("Enter total hindi books: "))
        self.Other_books = int(input("Enter total other books: "))
        self.DispBooks()
    def ComputeBooks(self):
        self.Total = self.English_books + self.Hindi_books + self.Other_books
        return self.Total
    def DispBooks(self):
        print ("Book informatio...")
        print("Name: ", self.Name)
        print("English books: ", self.English_books)
        print("Hindi books: ", self.Hindi_books)
        print("Other books: ", self.Other_books)
        print("Total books: ", self.ComputeBooks())
                
Bk = Library()
Bk.ReadBooks()

        			
