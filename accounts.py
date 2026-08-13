import storage

class BankAccount:
    def __init__(self, first_name, last_name, age, email, contact, hashed_pin, account_number, balance):
        #Personal details
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.contact_info = contact

        #Security and Account details
        self.hashed_pin = hashed_pin
        self.acct_num = account_number

        #Financial detail
        self.balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return storage.update_balance(self.acct_num, self.balance)
        else:
            return False

    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return storage.update_balance(self.acct_num, self.balance)
        else:
            return False

    def check_balance(self):
        return self.balance 