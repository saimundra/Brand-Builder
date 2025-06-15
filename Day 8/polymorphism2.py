#task:
#bank account system
#create a comprehensive bank account system that demonstrates inheritance and polymorphism
list1 = ["debited","credited","credited","debited"]
class BankAccount:
    def __init__(self,account_number,account_holder,balance,transaction_history,initial_deposit):
        self.account_number = account_number
        self.account_holder = account_holder
        self.transaction_history = list1
        self.balance = float(balance)
        self.initial_deposit = 0
      
    def checkbalance(self):
      self.balance =   self.initial_deposit + self.balance 

    def deposit(self,amount):
       self.balance = self.balance + amount
       depositMsg = f"User deposited {amount}"
       self.transaction_history.append(depositMsg)

    def withdraw(self,amount):
       self.balance = self.balance - amount

    def get_transaction_history(self):
       return self.transaction_history  
    
    def calculate_interest(self,interest_rate):
       print("interest of the total sum is:"(self.balance * interest_rate/100))
class SavingAccount(BankAccount):
   def __init__(self,account_number,account_holder,balance,interest_rate, interest_amt, interest_monthly ):
      super().__init__(account_number,account_holder,balance)
      self.interest_rate = 2.5 #anually
      self.balance = 100
      self.interest_amt = interest_amt #annually
      self.interest_monthly = interest_monthly #monthly

   def withdraw(self,amount):
     if(self.balance < 100):
      print("amount too low!!")
     else:
      self.balance = self.balance - amount
      withdrawMsg = f"User withdrew {amount}"
      self.transaction_history.append(withdrawMsg)

   def calculate_interest(self):
    self.interest_amt = (self.balance * self.interest_rate* 12)/100

   def monthly_interest(self):
    self.interest_monthly = self.interest_amt/12

   def applymonthly_interest(self):
      self.balance = self.interest_monthly + self.balance
         
class CheckingAccount(BankAccount):
  def __init__(self, account_number, account_holder, balance,overdraft_limit):
    super().__init__(account_number, account_holder, balance )
    self.overdraftlimit = overdraft_limit
    self.overdraftlimit = 200
  def withdraw(self,amount):
    self.balance = self.balance + self.overdraftlimit

customer1 = SavingAccount("123a","saimundra",2000)
customer1.deposit(2000)
customer1.get_transaction_history()
print(customer1.calculate_interest())



