# Yatube API project
##### _Made by the one and only [Sasha Smirnov][github_link]_
# 

## Что такое API Yatube

### API Yatube - это интерфейс взаимодействия с данными социальной сети Yatube

API Yatube позволяет Вам:

- Взаимодействовать с объектами базы данных Yatube: пользователями, подписками, постами, комментариями к ним, сообществами
- Писать посты, оставлять комментарии, регистрировать новых пользователей, подписываться на других пользователей
- Получать информацию о вышеперечисленных объектах ресурса
- Изменять и удалять объекты ресурса при наличии соответствующих прав доступа

## Stack

- [Python3.7]
- [Django 2.2.16]
- [Django REST framework][drf]

## Запуск проекта
- Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone https://github.com/crush-on-anechka/api_final_yatube
cd api_final_yatube
``` 
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

Некоторые примеры запросов к API:
- Запрос на получение поста с идентификатором "1":
```
GET 127.0.0.1:8000/api/v1/posts/1/
```
- Ответ:
```
{
    "author": "admin",
    "group": null,
    "id": 1,
    "image": null,
    "pub_date": "2022-08-05T14:24:54.369098Z",
    "text": "sdfdsf"
}
```
- Получение JWT токена для зарегистрированного пользователя:
```
POST 127.0.0.1:8000/api/v1/jwt/create/ username="user01" password="qwerty123"
```
- Ответ:
```
{
    "access": <your_access_token>,
    "refresh": <your_refresh_token>
}
```

## Эндпоинты и фичи

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
GET /api/v1/posts?limit=5&offset=10
```
- Поиск подписчиков текущего пользователя:
```
GET /api/v1/follow/?search=aleks
```

Замечания и пожелания направляйте напрямую [Владимиру Путину][vp]

[github_link]: <http://github.com/crush-on-anechka>
[python3.7]: <https://docs.python.org/3.7/whatsnew/3.7.html>
[Django 2.2.16]: <https://docs.djangoproject.com/en/4.0/releases/2.2.16/>
[drf]: <https://www.django-rest-framework.org>
[vp]: <http://www.kremlin.ru>
