from app.calculations import add, sub, mult, quot, BankAccount
import pytest


@pytest.fixture
def zero_bank_account():
    print("Creating zero-balance bank account.")
    return BankAccount()


@pytest.fixture
def bank_account():
    print("Creating 50 balance bank account.")
    return BankAccount(50)


@pytest.mark.parametrize("n1, n2, expected", [
    (1, 2, 3),
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(n1, n2, expected):
    print("Testing add...")
    assert add(n1, n2) == expected


@pytest.mark.parametrize("n1, n2, expected", [
    (2, 1, 1),
    (5, 2, 3),
    (7, 1, 6),
    (12, 4, 8)
])
def test_sub(n1, n2, expected):
    print("Testing sub...")
    assert sub(n1, n2) == expected


@pytest.mark.parametrize("n1, n2, expected", [
    (1, 2, 2),
    (3, 2, 6),
    (7, 1, 7),
    (12, 4, 48)
])
def test_mult(n1, n2, expected):
    print("Testing mult...")
    assert mult(n1, n2) == expected


@pytest.mark.parametrize("n1, n2, expected", [
    (10, 2, 5),
    (30, 3, 10),
    (15, 5, 3),
    (12, 4, 3)
])
def test_div(n1, n2, expected):
    print("Testing quot...")
    assert quot(n1, n2) == expected


def test_bank_set_default_amount(zero_bank_account):
    print("Testing default amount for BankAccount.")
    assert zero_bank_account.balance == 0


def test_bank_set_initial_amount(bank_account):
    print("Testing initial amount for BankAccount.")
    assert bank_account.balance == 50


def test_withdraw(bank_account):
    print("Testing withdraw for BankAccount.")
    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_deposit(bank_account):
    print("Testing deposit for BankAccount.")
    bank_account.deposit(30)
    assert bank_account.balance == 80


def test_collect_interest(bank_account):
    print("Testing collect interest for BankAccount.")
    bank_account.collect_interest()
    assert bank_account.balance == 55
