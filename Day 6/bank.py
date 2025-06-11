#create a bankaccount class with:
#attribute:account number, account holdername, balance
#methods: deposit,withdraw,checkbalance

class bank:
    def __init__(self,accNum,accName,balance):
        self.accNum = accNum
        self.accName = accName
        self.balance = balance

    def checkbalance(self):
        return self.balance
    
    def deposit(self, depositamt):
        self.balance = self.balance + depositamt

    def withdraw(self, withdrawamt):
        if(withdrawamt > self.balance):
            print("you cannot withdraw this amount")
        else:
            self.balance = self.balance - withdrawamt
    