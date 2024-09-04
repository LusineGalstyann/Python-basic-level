class BankAccount():
    def __init__(self,account_number,owner,balance=0.0,currency='USD'):
        self.account_number=account_number
        self.balance=balance
        self.owner=owner
        self.currency=currency

    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def get_balance(self):
        return self.balance
    def get_account_info(self):
        str_info=f"Account number is: {self.account_number},account owner is: {self.owner}, and account balance is: {self.balance}"
        return str_info

account1 = BankAccount("123456789", "Anna")
print(account1.get_account_info())

account1.deposit(1000)
account1.withdraw(500)
print(account1.get_account_info())