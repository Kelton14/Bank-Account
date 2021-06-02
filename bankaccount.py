class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance <= amount):
            print("Insufficient funds: charging a $5 fee")
            self.balance -= 5
        else: 
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            x = self.balance * self.int_rate
            self.balance += x
        else: 
            self.balance = self.balance
        return self
    
Account1 = BankAccount(.03, 500)
Account2 = BankAccount(.01, 150)
Account3 = BankAccount(.06, 1000)

Account1.deposit(100).deposit(500).deposit(5).withdraw(10).yield_interest().display_account_info()

Account2.deposit(150).deposit(100).withdraw(50).withdraw(30).withdraw(10).withdraw(25).yield_interest().display_account_info()