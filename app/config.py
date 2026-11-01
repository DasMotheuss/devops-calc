"""Конфігурація з змінних середовища (секрети не зберігаються в коді)."""
import os


def get_config() -> dict:
    return {
        "env": os.getenv("APP_ENV", "development"),
        # Секрет передається з GitHub Secrets; у коді лише перевіряємо його наявність
        "secret_configured": bool(os.getenv("APP_SECRET_KEY")),
    }
