class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        # increases the account balance by the given amount
        self.balance += amount
        return self
    def withdraw(self, amount):
        # decreases the account balance by the given amount if there are sufficient funds; 
        # if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        if self.balance > 0:
            self.balance -= amount
        elif self.balance < 5.00:
            self.balance -= 5.00
            print('Insufficent Funds: Charging a $5 fee')
        return self
    def display_account_info(self):
        # print to the console: eg. "Balance: $100"
        print('Balance:',self.balance)
        return self
    def yield_interest(self):
        # increases the account balance by the current balance 
        # * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance = (self.balance + (self.balance * self.int_rate))
        return self
        # increases the account balance by the current balance 
        # * the interest rate (as long as the balance is positive)

# 3 Accounts for testing purposes
logan = BankAccount(0.01, 0)
jac = BankAccount(0.01, 0)
dave = BankAccount(0.01, 0)

# Testing our BankAccount class's with it's functions 
logan.deposit(1000).deposit(500).deposit(100).withdraw(120).yield_interest().display_account_info()
# interest rate = 16.10 // balance = 1494.80
jac.deposit(500).deposit(500).withdraw(10).withdraw(10).withdraw(10).withdraw(10).yield_interest().display_account_info()
# interest rate = 8 // balance = 969.60
dave.deposit(5).deposit(5).deposit(10).withdraw(2).yield_interest().display_account_info()
# interest rate = 8 // balance = 18.18




