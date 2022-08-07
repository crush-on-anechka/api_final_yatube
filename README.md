# Yatube API project
##### _Made by the one and only [Sasha Smirnov][github_link]_
# 

## Что такое API Yatube

### API Yatube - это интерфейс взаимодействия с базой данных соцсети Yatube

API Yatube позволяет Вам:

- Взаимодействовать с объектами базы данных Yatube: пользователямми, подписками, постами, комментариями к ним, сообществами
- Писать посты, оставлять комментарии, регистрировать новых пользователей, подписываться на других пользователей
- Получать информацию о вышеперечисленных объектах ресурса
- Изменять и удалять объекты ресурса при наличии соответствующих прав доступа

## Stack

- Python 3.7[python3.7]
- Django 2.2.16[django]
- Django REST framework[drf]

## Запуск проекта
- Установите и запустите виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
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

[github_link]: <http://github.com/crush-on-anechka>
[python3.7]: <https://docs.python.org/3.7/whatsnew/3.7.html>
[django]: <https://docs.djangoproject.com/en/4.0/releases/2.2.16/>
[drf]: <https://www.django-rest-framework.org>
