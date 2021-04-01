# tp-lab-2

## Запущенный instance

- https://tp-lab-2.herokuapp.com/
- http://store.coolprojects.online

## Диаграммы

https://drive.google.com/drive/folders/1ohmbabEa0AdgOPJHetOZmj0J6FkBLTZE?usp=sharing


## Как запустить локально

Способ, который всегда работает

1. удалить все файлы в папках migrate кроме `__init__.py`
2. удалить базу `db.sqlite3`
3. `python manage.py makemigrations`
4. `python manage.py migrate`
5. `python manage.py runserver`
