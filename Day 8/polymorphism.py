#polymorphism overrides the data in the child class from the parent class
"""
Task : Bank Account System (Basic Version)
Create a simple bank account system that demonstrates inheritance and polymorphism.
Base Class: BankAccount
Create a BankAccount base class with:
Attributes:

account_number (string)
owner_name (string)
balance (float, starts at 0)

"""

#bank account system
class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = 0 #default balance is 0
    def deposit(self, depositAmt):
        self.balance += depositAmt
    def withdrawamt (self,amount):
         if(self.balance  < 50):
             print("balance too low cant withdraw")
         else:
             self.balance = self.balance - amount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = 3.0

    def calculate_interest(self):
         print(self.balance , self.interest_rate)
         return (self.balance * self.interest_rate/100)
    
    def checkbalance (self):
        print(f"The total amount in your account is {self.balance}")
    
class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance, overdraft_limit):
        super().__init__(account_number, owner_name, balance)
        self.overdraft_limit = overdraft_limit
        self.overdraft_limit = 200

    def withdrawamt(self,amount):
        if(self.balance + self.overdraft_limit <= amount):
            self.balance = self.balance - amount
        else:
            print("you are out of your limit")

customer1 = SavingsAccount("1234q","ram",2000)
print(customer1.calculate_interest()) #calculate interest

customer1.withdrawamt(500)
customer1.checkbalance()
   

        







