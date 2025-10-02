class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the given amount into the account."""
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw the given amount if funds are sufficient."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
