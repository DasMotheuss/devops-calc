"""Бізнес-логіка: прості арифметичні операції."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Ділення на нуль неможливе")
    return a / b


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculate(expression: str) -> float:
    """Обчислює вираз виду '2 + 3' (два числа й оператор через пробіл)."""
    parts = expression.split()
    if len(parts) != 3 or parts[1] not in OPERATIONS:
        raise ValueError(f"Некоректний вираз: {expression!r}")
    a, op, b = float(parts[0]), parts[1], float(parts[2])
    return OPERATIONS[op](a, b)
