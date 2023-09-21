from app.calculations import add, sub, mult, quot


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(3, 1) == 2


def test_mult():
    assert mult(3, 2) == 6


def test_div():
    assert quot(10, 2) == 5


test_add()