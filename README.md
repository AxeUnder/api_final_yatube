# api_final_yatube

## Описание
Это api по сути является backend-приложением к проекту yatube (соц. сети), которое позволяет отправлять запросы (GET, POST, PATCH, PUT и DELETE) на сервер к базе данных приложения. С их помощью можно запросить список постов или авторизовавшись опубликовать собственный.

**Инструменты и стек**:** #Python #Django #API #RestFramework #JWTAuthentication #Djoser #Pillow #PyCharm #Postman

## Возможности
**GET `http://127.0.0.1:8000/api/v1/posts/`**
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
**POST `http://127.0.0.1:8000/api/v1/posts/`**
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
**Response samples**
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
Реализована возможность создавать пользователя и получать JWT-токен.
**POST `http://127.0.0.1:8000/api/v1/jwt/create/`**
```json
{
  "username": "string",
  "password": "string"
}
```
**Response samples**
```json
{
  "refresh": "string",
  "access": "string"
}
```
Можно комментировать посты и подписываться на авторов.
**POST `http://127.0.0.1:8000/api/v1/follow/`**
```json
{
  "following": "string"
}
```
**Response samples**
```json
{
  "user": "string",
  "following": "string"
}
```
**POST `http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/`**
```json
{
"text": "string"
}
```
**Response samples**
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/AxeUnder/api_final_yatube.git
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv env
source env/bin/activate
```

Установить зависимости из файла **requirements.txt**:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:
```bash
python3 manage.py migrate
```

Запустить проект:
```bash
cd yatube_api
python3 manage.py runserver
```


#№ Примеры запросов

Вывод списка постов:
`/api/v1/posts/`

Детали поста:
`/api/v1/posts/{post_id}/`

Вывод списка комментариев к посту:
`/api/v1/posts/{post_id}/comments/`

Документация:
`/redoc/`

## Об авторе
Python-разработчик
> [AxeUnder](https://github.com/AxeUnder).
