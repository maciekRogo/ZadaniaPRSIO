class BankAccount:
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = str(owner)
    def deposit(self, ile):
        self.balance += ile
    def withdraw(self, ile):
        if self.balance >= ile:
            self.balance -= ile
        else:
            print(f"Nie ma pieniędzy na koncie aby wypłacić {ile} zł")

bankowe1 = BankAccount(123,2137,"Andrzej Duda")
print(bankowe1.balance)
for x in range(10):
    bankowe1.deposit(1)
print(bankowe1.balance)
for x in range(10):
    bankowe1.withdraw(1)
print(bankowe1.balance)



