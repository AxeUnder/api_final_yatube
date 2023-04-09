# api_final
#api final

Это api по сути является backend-приложением к проекту yatube, которое позволяет отправлять запросы (GET, POST, PATCH, PUT и DELETE) на сервер к базе данных приложения. С их помощью можно запросить список постов или авторизовавшись опубликовать собственный.
Реализована возможность создавать пользователя и получать JWT-токен. Можно комментировать посты и подписываться на авторов.

##Технологии:
```
- Python;
- Django;
- Rest Framework;
- JWTAuthentication;
- djoser;
```

#Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:
`git clone https://github.com/Digital-Stalker/api_final_yatube.git
cd api_final_yatube`

Cоздать и активировать виртуальное окружение:
`python3 -m venv env
source env/bin/activate`

Установить зависимости из файла **requirements.txt**:
`python3 -m pip install --upgrade pip
pip install -r requirements.txt`

Выполнить миграции:
`python3 manage.py migrate`

Запустить проект:
`cd yatube_api
python3 manage.py runserver`


#Примеры запросов

Вывод списка постов:
`/api/v1/posts/`

Детали поста:
`/api/v1/posts/{post_id}/`

Вывод списка комментариев к посту:
`/api/v1/posts/{post_id}/comments/`

Документация:
`/redoc/`
