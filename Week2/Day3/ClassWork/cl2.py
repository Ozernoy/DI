'''

Exercise: Bank Account Management System
Overview
You will create an  BankAccount class that represents a bank account with advanced features. This class will manage different account types, track transactions, and include more complex class methods for account management.
Requirements
1. *Class Attributes and Methods*:
   - The class should keep track of the total number of bank accounts created and maintain a list of all accounts.
   - Implement a class method to find an account by its account number.
   - Implement a class method to summarize total balances across all accounts.
2. *Instance Attributes and Methods*:
   - Use a @property to manage access to the account balance.
   - Use a @property and @setter to handle and validate the account type.
   - Include a transaction history that logs deposits and withdrawals.
   - Implement a method to calculate and add interest to the account balance (specific to savings accounts).
   - Implement methods for depositing and withdrawing money, with validation checks.
Implementation Details
1. *Class Attributes*:
   - total_accounts: Tracks the total number of bank accounts created.
   - all_accounts: A list that stores references to all BankAccount instances.
   - interest_rate: A class attribute to define the default interest rate for savings accounts.
2. *Class Methods*:
   - get_total_accounts(cls): Returns the total number of accounts.
   - find_account_by_number(cls, account_number): Finds and returns an account by its account number.
   - total_balances(cls): Returns the sum of balances across all accounts.
3. *Properties*:
   - balance: Provides access to the account balance.
   - account_type: Manages the type of account with validation logic.
   - transaction_history: A list that logs all transactions (deposits and withdrawals).
4. *Methods*:
   - deposit(amount): Adds money to the account and logs the transaction.
   - withdraw(amount): Withdraws money, ensuring the balance doesn’t go negative, and logs the transaction.
   - apply_interest(): Applies interest to savings accounts.
Tasks to Complete
1. *Create the BankAccount class* with the provided class and instance attributes.
2. *Implement class methods* to manage and interact with the accounts collectively.
3. *Implement the @property and @setter* for the account balance and account type.
4. *Track transaction history* within each account.
5. *Test your class* by creating multiple accounts, performing various transactions, and applying interest.
Expected Output
When you run the example usage:
- The account balances should update correctly based on deposits, withdrawals, and interest application.
- The total number of accounts created and total balances should be tracked and displayed accurately.
- The find_account_by_number method should correctly identify accounts by their unique account number.
- The transaction history for each account should log all actions taken. (
'''

class BankAccount:

    def __init__(self, total_accounts, interest_rate, all_accounts = None):
        if all_accounts is None:
            self.all_accounts = []  # Default to an empty list if no list is provided
        else:
            self.all_accounts = all_accounts  # Initialize with the provided list
        self.total_accounts = total_accounts
        self.interest_rate = interest_rate

    def get_total_accounts(self):
        return self.total_accounts
    
    def find_account_by_number(self, account_number):
        return self.all_accounts[account_number]
    
    def total_balances(self):
        return sum(self.all_accounts)
    
    @property
    def balance(self):
        pass

    @property
    def account_type(self):
        