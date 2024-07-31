class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        if amount == 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance += amount

    def transfer(self, receiver, amount):
        if not (receiver):
            raise ValueError("Receiving account doesn't exist")
        self.withdraw(amount)
        receiver.deposit(amount)