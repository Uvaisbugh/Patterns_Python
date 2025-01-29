class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance  # Making balance private

        print(f"Account created successfully for {self.name}.")
        print(f"Initial balance: 💲{self._balance}")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Successfully deposited 💲{amount}.")
            print(f"Your new balance is 💲{self._balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdrawal(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Withdrawal of 💲{amount} successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def account_balance(self):
        print(f"Mr. {self.name}, your account balance is 💲{self._balance}.")

    def transfer(self, amount, target_account):
        """Transfer money to another BankAccount object"""
        if isinstance(target_account, BankAccount):
            if self._balance >= amount and amount > 0:
                self._balance -= amount
                target_account._balance += amount
                print(f"Successfully transferred 💲{amount} to {target_account.name}.")
                print(f"Your new balance is 💲{self._balance}.")
                target_account.account_balance()
            else:
                print("Insufficient balance or invalid amount.")
        else:
            print("Target account must be a BankAccount instance.")

    def __str__(self):
        return f"Account owner: {self.name}, Balance: 💲{self._balance}"

# Example usage
Jose = BankAccount("Uvais", 200)
Jose.deposit(500)
Jose.withdrawal(150)
Jose.account_balance()

# Transfer money between accounts
Ali = BankAccount("Ali", 1000)
Jose.transfer(200, Ali)

print(Ali)
print(Jose)
