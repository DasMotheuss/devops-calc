"""Збирає статичну сторінку застосунку в dist/site для деплою на GitHub Pages."""
import datetime
import os
import pathlib

from app import __version__
from app.calculator import calculate

out = pathlib.Path("dist/site")
out.mkdir(parents=True, exist_ok=True)
examples = ["2 + 3", "10 / 4", "6 * 7", "9 - 12"]
rows = "".join(f"<tr><td>{e}</td><td>{calculate(e)}</td></tr>" for e in examples)
commit = os.getenv("GITHUB_SHA", "local")[:7]
built = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
html = f"""<!doctype html><html lang="uk"><head><meta charset="utf-8">
<title>devops-calc {__version__}</title>
<style>body{{font-family:sans-serif;max-width:640px;margin:40px auto}}
td,th{{border:1px solid #ccc;padding:6px 12px}}table{{border-collapse:collapse}}</style></head>
<body><h1>devops-calc v{__version__}</h1>
<p>Сторінку автоматично зібрано й розгорнуто GitHub Actions.</p>
<p>Коміт: <code>{commit}</code>, збірка: {built}</p>
<table><tr><th>Вираз</th><th>Результат</th></tr>{rows}</table></body></html>"""
(out / "index.html").write_text(html, encoding="utf-8")
print(f"Site built: {out / 'index.html'}")
