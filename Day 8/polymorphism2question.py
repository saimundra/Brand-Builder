"""Task 7: Bank Account System (Detailed - Updated)

Create a comprehensive bank account system that demonstrates inheritance and polymorphism.

### Base Class: BankAccount
Create a BankAccount base class with:

*Attributes:*
- account_number (string)
- account_holder (string) 
- balance (float, starts at 0)
- transaction_history (list to store transaction records)

*Methods:*
- __init__(account_number, account_holder, initial_deposit=0)
- deposit(amount) - adds money to account, records transaction
- withdraw(amount) - basic withdrawal (may be overridden), records transaction
- get_balance() - returns current balance
- get_transaction_history() - returns list of all transactions
- calculate_interest() - abstract method to be implemented by subclasses

### Subclass 1: SavingsAccount
Inherits from BankAccount with these specifics:

*Additional Attributes:*
- interest_rate (default 2.5% annually)
- minimum_balance (default $100)

*Overridden/New Methods:*
- withdraw(amount) - prevents withdrawal if it would drop below minimum balance
- calculate_interest() - calculates monthly interest: balance * (interest_rate / 12 / 100)
- apply_monthly_interest() - adds calculated interest to balance

*Rules:*
- Cannot withdraw if balance would go below minimum balance
- Earns interest monthly
- No withdrawal fees

### Subclass 2: CheckingAccount
Inherits from BankAccount with these specifics:

*Additional Attributes:*
- overdraft_limit (default $500)
- transaction_fee (default $2 for withdrawals over $1000)
- monthly_fee (default $10)

*Overridden/New Methods:*
- withdraw(amount) - allows overdraft up to limit, applies fees when applicable
- calculate_interest() - no interest earned (returns 0)
- apply_monthly_fee() - deducts monthly maintenance fee
- check_overdraft() - returns True if account is overdrawn

*Rules:*
- Can go negative up to overdraft limit
- Charges $2 fee for withdrawals over $1000
- Charges $10 monthly maintenance fee
- No interest earned

### Polymorphism Demonstration
Create a Bank class that manages multiple accounts:

*Methods:*
- add_account(account) - adds any type of BankAccount
- process_monthly_operations() - applies interest/fees to all accounts
- get_total_deposits() - sums all positive balances
- generate_bank_report() - shows summary of all accounts

### Requirements:
1. All monetary amounts should be rounded to 2 decimal places
2. Transaction history should include: date, type (deposit/withdrawal/fee/interest), amount, balance after transaction
3. Include proper error handling (negative deposits, insufficient funds, etc.)
4. Demonstrate polymorphism by calling the same methods on different account types

### Sample Usage:
python
# Create different account types
savings = SavingsAccount("SAV001", "Alice Smith", 1000)
checking = CheckingAccount("CHK001", "Bob Jones", 500)

# Create bank and add accounts
bank = Bank()
bank.add_account(savings)
bank.add_account(checking)

# Perform operations
savings.deposit(200)
checking.withdraw(1500)  # Should apply fee
bank.process_monthly_operations()  # Apply interest/fees to all

# Generate report
bank.generate_bank_report()


 """