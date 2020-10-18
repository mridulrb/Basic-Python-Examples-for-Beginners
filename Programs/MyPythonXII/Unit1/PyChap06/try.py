# File name: ...\\MyPythonXII\Unit1\PyChap06\try.py
class Friend:
    def accessible(self):
        print("You can access me.")
    def __inaccessible(self):
        print("You cann't access me.")

Friend().accessible()
Friend().__inaccessible()
#Friend()._Friend__inaccessible()
