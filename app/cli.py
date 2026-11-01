"""Запуск: python -m app.cli "2 + 3" """
import sys

from app.calculator import calculate


def main() -> None:
    expr = " ".join(sys.argv[1:]) or "2 + 3"
    print(f"{expr} = {calculate(expr)}")


if __name__ == "__main__":
    main()
