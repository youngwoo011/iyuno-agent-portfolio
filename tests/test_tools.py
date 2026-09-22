from app.tools import calculator


def test_add():
    assert calculator(2, 3, "add") == 5


def test_subtract():
    assert calculator(10, 4, "subtract") == 6


def test_multiply():
    assert calculator(5, 6, "multiply") == 30


def test_divide():
    assert calculator(20, 4, "divide") == 5


def test_divide_by_zero():
    assert calculator(10, 0, "divide") == "0으로 나눌 수 없습니다."