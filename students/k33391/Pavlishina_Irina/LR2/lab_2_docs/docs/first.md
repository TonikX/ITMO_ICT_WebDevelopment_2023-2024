# Настройки приложения/сервера


В дефолтные параметры, определяемые в settings.py, внесены два изменения:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ##
    'flights.apps.FlightsConfig'
]

```

для того, что бы подключть приложение. И:

```
AUTH_USER_MODEL = 'flights.Passenger'
```
для переопределения пмодели юзера.


Так же добавлен новый корень для юрл-адресов нового приложения

```

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('flights.urls'))
]

```