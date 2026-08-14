import storage
import transactions

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
            deposit_update = storage.update_balance(self.acct_num, self.balance)
            if deposit_update:
                return transactions.log_transaction(self.acct_num, "DEPOSIT", amount, self.check_balance())
        else:
            return False

    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            withdrawal_update = storage.update_balance(self.acct_num, self.balance)
            if withdrawal_update:
                return transactions.log_transaction(self.acct_num, "WITHDRAWAL", amount, self.check_balance())
        else:
            return False

    def check_balance(self):
        return self.balance 

    def read_txns(self):
        return transactions.display_txn_history(self.acct_num)