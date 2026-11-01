# devops-calc

Навчальний проєкт для практичної роботи 10 і модульної контрольної 5 (DevOps, CI/CD на GitHub Actions).
Автор: Шпильовий Максим Максимович, група МІП-1-25-1.4-д.

* `app/` - застосунок (калькулятор)
* `tests/` - автотести pytest
* `scripts/build_site.py` - збирання статичної сторінки
* `.github/workflows/main.yml` - конвеєр: build -> test -> release -> deploy

Локальний запуск:

    pip install -r requirements.txt
    pytest -v
    python -m app.cli "6 * 7"
