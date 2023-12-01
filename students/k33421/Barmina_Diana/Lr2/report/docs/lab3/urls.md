# Пути

**Все загруженные приложения**</br>

```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "alpinism_app",
    "djoser",
    "django_filters",
]
```

**Дополнительные настройки для REST FRAMEWORK**</br>
<br/> <li> В DEFAULT_AUTHENTICATION_CLASSES добавлена аутентификация пользователя по токену
<li>В DEFAULT_FILTER_BACKENDS добавлена настройка фильтров
<li>В DEFAULT_PERMISSION_CLASSES добавлена проверка на аутентификацию пользователя 

```

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),

    'DEFAULT_FILTER_BACKENDS':
        ['django_filters.rest_framework.DjangoFilterBackend'],


    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

```
**Настройка Djoser для аутентификации**</br>

```

DJOSER = {
    "USER_ID_FIELD": "username"
}

```