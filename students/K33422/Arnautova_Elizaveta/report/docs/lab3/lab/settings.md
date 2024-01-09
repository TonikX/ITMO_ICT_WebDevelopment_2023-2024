**Settings:** 

Добавлена возможность зарегистрироваться на страничке, а также прописаны базовые разрешения
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}
```
Список доустановленных приложений:
```
INSTALLED_APPS = [
    ...
    "rest_framework",
    "rest_framework.authtoken",
    'mountaineeringclub_app',
    "djoser",
    ...
]
```