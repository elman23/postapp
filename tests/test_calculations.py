from app.calculations import add, sub, mult, quot, BankAccount
import pytest


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


def test_bank_set_initial_amount():
    bank_account = BankAccount(50)
    assert bank_account.balance == 50


def test_bank_set_default_amount():
    bank_account = BankAccount()
    assert bank_account.balance == 0


def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_deposit():
    bank_account = BankAccount(50)
    bank_account.deposit(30)
    assert bank_account.balance == 80


def test_collect_interest():
    bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert bank_account.balance == 55
