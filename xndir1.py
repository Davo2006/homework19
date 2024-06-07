#xndir_1 (Bank account)
class BankAccount:
    def __init__(self,account_holder,balance:int = 0):
        self.account_holder = account_holder
        self.balance = balance
    @property
    def get_balance(self):
        return self.balance
    @get_balance.setter
    def get_balance(self):
        if self.balance < 0:
            return "Your balance is lowwer zero"
    def deposit(self,x):
        self.balance += x
        return f"{self.account_holder}'s balance is {self.balance}"
    def withdraw(self,y):
        self.balance -= y
        return f"{self.account_holder}'s balance is {self.balance}"
account_1 = BankAccount("Ronaldo",1000)
print(account_1.get_balance)