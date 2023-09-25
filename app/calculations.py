def add(n1: int, n2: int):
    return n1 + n2


def sub(n1: int, n2: int):
    return n1 - n2


def mult(n1: int, n2: int):
    return n1 * n2


def quot(n1: int, n2: int):
    return n1 / n2


class InsufficientAmountException(Exception):
    pass


class BankAccount():
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientAmountException("Insufficient money in the account!")
        self.balance -= amount

    def collect_interest(self):
        self.balance = round(self.balance * 1.1, 2)
