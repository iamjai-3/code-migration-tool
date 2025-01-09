class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Amount must be positive"

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdrew ${amount}. New balance: ${self.balance}"
            return "Insufficient funds"
        return "Amount must be positive"

    def get_balance(self):
        return f"Current balance: ${self.balance}"


# Example usage:
if __name__ == "__main__":
    # Create a new account
    my_account = BankAccount("John Doe", 1000)

    # Perform some transactions
    print(my_account.get_balance())  # Current balance: $1000
    print(my_account.deposit(500))  # Deposited $500. New balance: $1500
    print(my_account.withdraw(200))  # Withdrew $200. New balance: $1300
    print(my_account.withdraw(2000))  # Insufficient funds
