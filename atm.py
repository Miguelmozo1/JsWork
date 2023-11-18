class BankAccount:
    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, cash):
        self.balance += cash
        print(self.balance)
        return self
    def withdraw(self, withdraw):
        self.balance -= withdraw
        print(self.balance)
        return self
    def display_accnt_info(self):
        print (f"Account Balance: {self.balance}")
        return self
    def int_increase(self):
        self.balance += self.balance * self.int_rate
        print(f'Account after Interest: {self.balance}')
        return self


class User:
    def __init__(self, full_name, zip_code):
        self.full_name = full_name
        self.zip_code = zip_code
        self.accnt = BankAccount(0, 0.05)
    def deposit(self, cash):
        self.accnt.balance += cash
        print(self.accnt.balance)
        return self
    def withdraw(self, withdraw):
        self.accnt.balance -= withdraw
        print(self.accnt.balance)
        return self
    def display_user_balance(self):
        self.accnt.balance += self.accnt.balance * self.accnt.int_rate
        print (f"Account Balance: {self.accnt.balance}")
        return self

accnt1 = User("Miguel Mozo", "911183")
accnt1.deposit(40).withdraw(30).display_user_balance()