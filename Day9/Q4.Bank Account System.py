class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rupees {amount}. New balance: Rupees {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew Rupees {amount}. New balance: Rupees {self.balance}")
    def display_balance(self):
        print(f"Account {self.account_number} Balance: Rupees {self.balance}")
acc = BankAccount("ACC12345", 50000)
acc.deposit(20000)
acc.withdraw(12000)
acc.display_balance()
