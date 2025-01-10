deposit(amount) {
    if (amount > 0) {
        this.balance += amount;
        return `Deposited $${amount}. New balance: $${this.balance}`;
    }
    return "Amount must be positive";
}

withdraw(amount) {
    if (amount > 0) {
        if (this.balance >= amount) {
            this.balance -= amount;
            return `Withdrew $${amount}. New balance: $${this.balance}`;
        }
        return "Insufficient funds";
    }
    return "Amount must be positive";
}