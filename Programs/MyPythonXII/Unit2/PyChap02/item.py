# File name: ...\\MyPythonXII\Unit2\PyChap02\item.py
class Item:
    ItemCode = ItemPrice = ItemQty = OfferPer = 0
    ItemName = " "
    def GetStock(self):
        print ("Enter item details...")
        self.ItemCode = int(input("Enter item code: "))
        self.ItemName = input("Enter item name: ")
        self.ItemPrice = int(input("Enter item price: "))
        self.ItemQty = int(input("Enter item quantity: "))
        self.GetOffer()
    def GetOffer(self):
        if self.ItemQty <= 100:
            self.OfferPer = 0
        elif self.ItemQty > 100 and self.ItemQty <= 200:
            self.OfferPer = 5
        elif self.ItemQty > 200:
            self.OfferPer = 10        
    def ShowItem(self):
        print ("Item details...")
        print("Item code:", self.ItemCode)
        print("Item name:", self.ItemName)
        print("Item price:", self.ItemPrice)
        print("Item quantity:", self.ItemQty)
        print("Offer percentage:", self.OfferPer)
I = Item()
I.GetStock()
I.ShowItem()

        			
