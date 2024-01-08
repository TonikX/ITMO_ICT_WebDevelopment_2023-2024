# Администрирование.
### Администратор должен иметь возможность указания времени заезда и результата средствами Django-admin.

###### Добавление приложения
```
INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    ]

```

###### Регистрация моделей admin.py

```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Race)
admin.site.register(models.Register)
admin.site.register(models.Comment)

```


###### Добавление страницы администратора
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main_app.urls")),
]
```

###### Создание суперюзера
```
python3 manage.py createsuperuser
```