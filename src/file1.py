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
