# Yatube API project
##### _Made by the one and only Sasha Smirnov_
# 

## Использование

API Yatube позволяет:

- Написать собственный frontend на основе реальной востребованной соцсети
- Козырнуть перед девушкой или потенциальным работодателем
- ???
- Profit!!

## Stack

- Python 3.7
- Django 2.2.16
- Django REST framework

## Запуск проекта
- Установите и запустите виртуальное окружение:
```
python3 -m venv venv
source env/bin/activate
``` 

- Установите зависимости:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
``` 
- Выполните миграции и запустите проект:
```
python3 manage.py migrate
python3 manage.py runserver
```
## Запросы к API

API дает доступ к постам, сообществам, комментариям к постам, пользователям, подписчикам пользователя.
- Базовые эндпоинты:
```
/api/v1/users
/api/v1/users/1/
/api/v1/posts/
/api/v1/posts/1/
/api/v1/groups/
/api/v1/groups/1/
/api/v1/posts/1/comments/
/api/v1/posts/1/comments/1/
/api/v1/follow/
/api/v1/follow/1/
```
- Пагинация при запросе постов:
```
/api/v1/posts?limit=5&offset=10
```
- Получение JWT токена для пользователя:
```
POST .../api/v1/jwt/create
```