from bank import bank

customer1 = bank("123a","saimundra",1000)

print(customer1.checkbalance())

customer1.withdraw(200) #withdraw200 from account
print(customer1.checkbalance()) 

customer1.deposit(500) #deposit 500 to the account
print(customer1.checkbalance())
