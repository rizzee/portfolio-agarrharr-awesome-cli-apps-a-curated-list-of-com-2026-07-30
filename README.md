# CLI Apps Explorer

Удобный инструмент для поиска и навигации по списку крутых консольных приложений. Вы можете просматривать инструменты по категориям (Academia, Weather, Security и др.) прямо в терминале.

## Запуск

Для работы необходим Python 3.8+.

```bash
# Клонируйте репозиторий
git clone https://github.com/youruser/cli-apps-explorer.git
cd cli-apps-explorer

# Установите зависимости
pip install -r requirements.txt

# Запустите приложение
python cli_apps.py
```

## Пример

После запуска вы можете использовать команды для поиска нужного софта:

```bash
# Показать все приложения в категории Weather
python cli_apps.py list weather

# Найти инструмент, связанный с Markdown
python cli_apps.py search markdown
```

## Тесты

Если вы вносите изменения в код, обязательно запустите тесты:

```bash
pytest -q
```
