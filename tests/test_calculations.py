from app.calculations import add, sub, mult, quot


def test_add():
    print("Testing add...")
    assert add(1, 2) == 3


def test_sub():
    print("Testing sub...")
    assert sub(3, 1) == 2


def test_mult():
    print("Testing mult...")
    assert mult(3, 2) == 6


def test_div():
    print("Testing quot...")
    assert quot(10, 2) == 5