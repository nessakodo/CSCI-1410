###########################################################################
# Name: Vanessa Benavente
# Date: July 24, 2023
###########################################################################

# Import the BankAccount class from BankAccount.py
from old.BankAccount import BankAccount

def main():
    # Create a BankAccount object
    account = BankAccount()

    # Ask user for the number of transactions
    num_transactions = int(input("Enter the number of transactions: "))
    completed_transactions = 0

    # Loop to handle each transaction
    for i in range(num_transactions):
        transaction_type = input("Enter transaction type (deposit/withdraw): ").lower()
        amount = float(input("Enter the amount for the transaction: "))

        if transaction_type == "deposit":
            if account.deposit(amount):
                completed_transactions += 1
                print(f"Deposit successful. Current balance: ${account.getBalance():.2f}")
            else:
                print("Error: Invalid deposit amount. Ignoring transaction.")

        elif transaction_type == "withdraw":
            if account.withdraw(amount):
                completed_transactions += 1
                print(f"Withdrawal successful. Current balance: ${account.getBalance():.2f}")
            else:
                print("Error: Insufficient balance. Ignoring transaction.")

        else:
            print("Error: Invalid transaction type. Ignoring transaction.")

    # Display the number of completed transactions and account balance
    print(f"\nNumber of completed transactions: {completed_transactions}")
    print(f"Final account balance: ${account.getBalance():.2f}")

if __name__ == "__main__":
    main()
