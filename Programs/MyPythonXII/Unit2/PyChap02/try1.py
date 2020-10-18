class ONE:
    one_no = 0
    one_name = " "
    def __init__(self):
        self.one_no = int(input("Enter for one: "))
        self.one_name = input("Enter name: ")
    def status(self):
        print(self.one_no, " ", self.one_name)
class TWO:
    two_no = 0
    two_name = " "
    two_salary = 0
    def __init__(self):
        self.two_no = int(input("Enter for two: "))
        self.two_name = input("Enter name:" )
        self.two_salary = float(input("Enter salary: "))
    def show(self):
        print(self.two_no, "-", self.two_name, "-", self.two_salary)
class THREE(ONE, TWO):
    three_no = 0
    Three_date = " "
    def __init__(self):
        self.three_no = int(input("Enter for 3: "))
        self.three_date = input("Enter date: ")
    def sales_detail(self):
        ONE.__init__(self)
        TWO.__init__(self)
TH = THREE()
TH.sales_detail()
