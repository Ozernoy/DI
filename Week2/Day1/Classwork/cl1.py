'''
Exercise: Implementing a Basic Bank Account Class
In this exercise, you will create a simple bank account system that allows users to deposit money, withdraw money, and check their account balance.
Step-by-Step Instructions:
1. *Define the Class:*
   - Create a class called BankAccount.
   - In the __init__ method, define two attributes: owner (the name of the account holder) and balance (the account balance, with a default value of 0).
2. *Create a Deposit Method:*
   - Define a method called deposit that accepts an amount as a parameter.
   - If the amount is positive, add it to the balance and print a message indicating the deposit and the new balance.
   - If the amount is not positive, print an error message.
3. *Create a Withdraw Method:*
   - Define a method called withdraw that accepts an amount as a parameter.
   - If the amount is greater than the current balance, print an error message indicating insufficient funds.
   - Otherwise, subtract the amount from the balance and print a message indicating the withdrawal and the new balance.
4. *Create a Check Balance Method:*
   - Define a method called check_balance that prints the current balance of the account.
5. *Test the Class:*
   - Create an instance of BankAccount with the owner's name as "Alice".
   - Use the deposit method to add 100 units to the account.
   - Use the withdraw method to subtract 30 units from the account.
   - Use the check_balance method to print the current balance.
#### Example Code:
Here is a template to get you started:
python
class BankAccount:
    def __init__(self, owner, balance=0):
        # Initialize the owner and balance attributes
        pass
    
    def deposit(self, amount):
        # Add the amount to the balance if it's positive, otherwise print an error
        pass
    
    def withdraw(self, amount):
        # Subtract the amount from the balance if it's within the available funds, otherwise print an error
        pass
    
    def check_balance(self):
        # Print the current balance
        pass

# Usage Example
account = BankAccount("Alice")
account.deposit(100)
account.withdraw(30)
account.check_balance()
Expected Output:
After implementing the methods, running the code should produce the following output:
100 deposited. New balance: 100
30 withdrawn. New balance: 70
Current balance: 70
'''


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('error')
    
    def withdraw(self, amount):
        # Subtract the amount from the balance if it's within the available funds, otherwise print an error
        if self.balance > amount:
            self.balance -= amount
        else:
            print('error')
    
    def check_balance(self):
        # Print the current balance
        print(self.balance)


account = BankAccount("Alice")
account.deposit(100)
account.withdraw(30)
account.check_balance()