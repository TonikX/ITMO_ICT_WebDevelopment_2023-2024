### settings.py


Файл `settings.py`- это настройки приложения, и они были в основном автоматически написаны при создании проекта.
Однако позднее вручную потребовалось внести некоторые изменения:

Во-первых, я указываю собственную модель пользователя, которую ранее определила в приложении conferences_app.

```
AUTH_USER_MODEL = 'conferences_app.Author'
```

Во вторых, определяю установленные приложения в проекте.
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'conferences_app'
]
```