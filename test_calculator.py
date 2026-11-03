"""Test cases for the Calculator class (run with: pytest)."""

import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# ---------- add ----------
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (-4, -6, -10),
    (0, 0, 0),
    (1.5, 2.5, 4.0),
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


# ---------- subtract ----------
@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (4, 10, -6),
    (-3, -3, 0),
    (5.5, 0.5, 5.0),
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


# ---------- multiply ----------
@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-2, 5, -10),
    (-2, -5, 10),
    (7, 0, 0),
    (0.5, 4, 2.0),
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


# ---------- divide ----------
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (7, 2, 3.5),
    (-9, 3, -3),
    (0, 5, 0),
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected


def test_divide_by_zero_raises(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)


def test_divide_floating_point(calc):
    assert calc.divide(1, 3) == pytest.approx(0.3333, rel=1e-3)


# ---------- power ----------
@pytest.mark.parametrize("base, exp, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (2, -1, 0.5),
    (9, 0.5, 3.0),
])
def test_power(calc, base, exp, expected):
    assert calc.power(base, exp) == expected


# ---------- modulo ----------
@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 1),
    (12, 4, 0),
    (-7, 3, 2),
])
def test_modulo(calc, a, b, expected):
    assert calc.modulo(a, b) == expected


def test_modulo_by_zero_raises(calc):
    with pytest.raises(ZeroDivisionError):
        calc.modulo(5, 0)


# ---------- square root ----------
@pytest.mark.parametrize("a, expected", [
    (16, 4),
    (0, 0),
    (2.25, 1.5),
])
def test_square_root(calc, a, expected):
    assert calc.square_root(a) == expected


def test_square_root_negative_raises(calc):
    with pytest.raises(ValueError):
        calc.square_root(-4)


# ---------- percentage ----------
@pytest.mark.parametrize("value, percent, expected", [
    (200, 10, 20),
    (50, 50, 25),
    (80, 0, 0),
])
def test_percentage(calc, value, percent, expected):
    assert calc.percentage(value, percent) == expected


# ---------- input validation ----------
@pytest.mark.parametrize("bad", ["5", None, [1], True])
def test_invalid_input_raises_type_error(calc, bad):
    with pytest.raises(TypeError):
        calc.add(bad, 1)


# ---------- history ----------
def test_history_records_operations(calc):
    calc.add(1, 2)
    calc.multiply(3, 4)
    assert calc.get_history() == [("1 + 2", 3), ("3 * 4", 12)]


def test_failed_operation_not_recorded(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)
    assert calc.get_history() == []


def test_clear_history(calc):
    calc.add(1, 1)
    calc.clear_history()
    assert calc.get_history() == []


def test_get_history_returns_copy(calc):
    calc.add(1, 1)
    calc.get_history().clear()
    assert len(calc.get_history()) == 1
