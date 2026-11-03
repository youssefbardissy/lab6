"""A simple calculator class with basic and extended operations."""

import math


class Calculator:
    """Performs arithmetic operations and keeps a history of results."""

    def __init__(self):
        self.history = []

    def _record(self, operation, result):
        self.history.append((operation, result))
        return result

    @staticmethod
    def _validate(*values):
        for v in values:
            if isinstance(v, bool) or not isinstance(v, (int, float)):
                raise TypeError(f"Expected a number, got {type(v).__name__}")

    def add(self, a, b):
        self._validate(a, b)
        return self._record(f"{a} + {b}", a + b)

    def subtract(self, a, b):
        self._validate(a, b)
        return self._record(f"{a} - {b}", a - b)

    def multiply(self, a, b):
        self._validate(a, b)
        return self._record(f"{a} * {b}", a * b)

    def divide(self, a, b):
        self._validate(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self._record(f"{a} / {b}", a / b)

    def power(self, base, exponent):
        self._validate(base, exponent)
        return self._record(f"{base} ** {exponent}", base ** exponent)

    def modulo(self, a, b):
        self._validate(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot take modulo by zero")
        return self._record(f"{a} % {b}", a % b)

    def square_root(self, a):
        self._validate(a)
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return self._record(f"sqrt({a})", math.sqrt(a))

    def percentage(self, value, percent):
        self._validate(value, percent)
        return self._record(f"{percent}% of {value}", value * percent / 100)

    def get_history(self):
        return list(self.history)

    def clear_history(self):
        self.history.clear()
