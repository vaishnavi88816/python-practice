class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
    
    def display_balance(self):
        print("Balance:", self.balance)

acc = BankAccount("Vijay", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.display_balance()


