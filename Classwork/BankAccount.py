###########################################################################
# Name: Vanessa Benavente
# Date: July 24, 2023
###########################################################################

class BankAccount:
    """Bank Account class with methods for deposits, withdrawals, and balance"""

    def __init__(self):
        """Initialize the bank account with a starting balance of 0"""
        self.balance = 0.0

    def deposit(self, amount):
        """Deposits money into the bank account.
        Returns True if the transaction is successful, False otherwise."""
        if amount >= 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        """Withdraws money from the bank account.
        Returns True if the transaction is successful, False otherwise."""
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def getBalance(self):
        """Returns the current amount of money in the account."""
        return self.balance
