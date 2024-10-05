class BankAccount:
    def __init__(self, account_balance=0.0) -> None:
        self.account_balance = account_balance
    def deposit(amount):
        self.account_balance += amount
    def withdraw(amount):
        if self.account_balance > amount:
            self.account_balance = self.account_balance - amount
            return True
        else:
            return False
        
    def display_balance():
        print(f"Current Balance: ${self.account_balance}")