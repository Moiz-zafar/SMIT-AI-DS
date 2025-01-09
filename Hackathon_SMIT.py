class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            print(f"Deposited {amount}. New balance: {self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount}")
            print(f"Withdrawn {amount}. New balance: {self.balance:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def transfer(self, amount, recipient_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Transferred: {amount} to {recipient_account}")
            print(f"Transferred {amount} to {recipient_account}. New balance: {self.balance:.2f}")
            return True
        else:
            print("Insufficient funds or invalid transfer amount.")
            return False

    def check_balance(self):
        print(f"Current balance for {self.account_holder_name}: {self.balance:.2f}")

    def account_statement(self):
        print(f"\nAccount Statement for {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)
        print(f"Current Balance: {self.balance:.2f}\n")

class Bank:
    def __init__(self):
        self.accounts = {}
        self.total_deposits = 0

    def create_account(self, account_holder, account_number):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, account_holder)
            print(f"Account created successfully for {account_holder}.")
        else:
            print(f"Account with number {account_number} already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def get_total_deposits(self):
        return self.total_deposits

    def get_total_accounts(self):
        return len(self.accounts)

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    bank = Bank()

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Check Balance")
        print("6. Account Statement")
        print("7. View Total Deposits") 
        print("8. View Total Accounts") 
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_holder = input("Enter account holder name: ").strip()
            account_number = input("Enter account number: ").strip()
            if account_holder and account_number:
                bank.create_account(account_holder, account_number)
            else:
                print("Account holder name and account number cannot be empty.")

        elif choice == '2':
            account_number = input("Enter account number: ").strip()
            account = bank.get_account(account_number)
            if account:
                amount = get_positive_float("Enter deposit amount: ")
                account.deposit(amount)
                bank.total_deposits += amount 
            else:
                print(f"Account with number {account_number} not found.")

        elif choice == '3':
            account_number = input("Enter account number: ").strip()
            account = bank.get_account(account_number)
            if account:
                amount = get_positive_float("Enter withdrawal amount: ")
                account.withdraw(amount)
            else:
                print(f"Account with number {account_number} not found.")

        elif choice == '4':
            sender_account_number = input("Enter your account number: ").strip()
            sender_account = bank.get_account(sender_account_number)
            if sender_account:
                recipient_account_number = input("Enter recipient's account number: ").strip()
                recipient_account = bank.get_account(recipient_account_number)
                if recipient_account:
                    amount = get_positive_float("Enter transfer amount: ")
                    if sender_account.transfer(amount, recipient_account_number):
                        recipient_account.deposit(amount) 
                else:
                    print(f"Recipient's account with number {recipient_account_number} not found.")
            else:
                print(f"Your account with number {sender_account_number} not found.")

        elif choice == '5':
            account_number = input("Enter account number: ").strip()
            account = bank.get_account(account_number)
            if account:
                account.check_balance()
            else:
                print(f"Account with number {account_number} not found.")

        elif choice == '6':
            account_number = input("Enter account number: ").strip()
            account = bank.get_account(account_number)
            if account:
                account.account_statement()
            else:
                print(f"Account with number {account_number} not found.")

        elif choice == '7':
            print(f"Total deposits in the bank: {bank.get_total_deposits():.2f}")

        elif choice == '8':
            print(f"Total number of accounts: {bank.get_total_accounts()}")

        elif choice == '9':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
