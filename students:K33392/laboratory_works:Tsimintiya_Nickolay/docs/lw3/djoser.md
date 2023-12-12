# Djoser 
Для реализации авторизации и регистрации по токенам будем использовать JWT (JSON Web Token). Для этого в settings.py добавим следующие настройки:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}
```

Теперь в urls.py добавим следующие пути:

```
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
```

## Пример работы 
Работа сервиса авторизации по токену будет продемонстрирована при помощи сервиса Postman 

Создание пользователя: 
![Иллюстрация к проекту](assets/register.png)

Получение токена пользователя:
![Иллюстрация к проекту](assets/token.png)
