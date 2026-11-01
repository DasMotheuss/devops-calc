import pytest

from app.calculator import add, subtract, multiply, divide, calculate
from app.config import get_config


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(9, 3) == 3


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


@pytest.mark.parametrize("expr, expected", [("2 + 3", 5), ("10 / 4", 2.5), ("3 * -2", -6)])
def test_calculate(expr, expected):
    assert calculate(expr) == expected


def test_calculate_invalid():
    with pytest.raises(ValueError):
        calculate("2 ^ 3")


def test_config_reads_env(monkeypatch):
    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.setenv("APP_SECRET_KEY", "dummy")
    cfg = get_config()
    assert cfg["env"] == "test"
    assert cfg["secret_configured"] is True
