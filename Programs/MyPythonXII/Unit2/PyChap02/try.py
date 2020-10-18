# File name: ...\\MyPythonXII\Unit2\PyChap01\try.py
class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance with the initial balance is zero."""
        self. customer = customer
        self. bank = bank
        self. account = acnt
        self. limit = limit
        self. balance = 0
    def get_customer(self):
        """Return name of the customer."""
        return self. customer
    def get_bank(self):
        """Return the bank s name."""
        return self. bank
    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self. account
    def get_limit(self):
        """Return current credit limit."""
        return self. limit
    def get_balance(self):
        """Return current balance."""
        return self. balance
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
       Return True if charge was processed; False if charge was denied."""
        if price + self. balance > self. limit: # if charge would exceed limit,
            return False # cannot accept charge
        else:
            self. balance += price
            return True
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self. balance -= amount

CrCard = CreditCard("A. N. Joshep", "SBI Saving", '30106534210', 1000)

wallet = [ ]
wallet.append(CreditCard('John Bowman', 'SBI Finance', '5ss6 5391', 4500))
wallet.append(CreditCard('John Bowman', 'SBI Credit', '5ss6 5391', 4500))
wallet.append(CreditCard('John Bowman', 'SBI Insurance', '5ss6 5391', 5500))

for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2*val)
    wallet[2].charge(3*val)

for c in range(3):
    print('Customer =', wallet[c].get_customer( ))
    print('Bank =', wallet[c].get_bank())
    print('Account =', wallet[c].get_account( ))
    print('Limit =', wallet[c].get_limit( ))
    print('Balance =', wallet[c].get_balance())
    while wallet[c].get_balance( ) > 100:
        wallet[c].make_payment(100)
        print('New balance =', wallet[c].get_balance())
    print( )
