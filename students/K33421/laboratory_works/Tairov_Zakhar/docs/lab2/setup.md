# Создание проекта
Установим фреймворк Django.

```commandline
pip install django
```

Создадим проект `racing` и приложение `racing_clib`:
```commandline
django-admin startproject racing .
cd racing
python manage.py startapp racing_club
```

Перейдём в файл `settings.py` и сделаем некоторые изменения:

- Добавим наше приложение в `INSTALLED_APPS`:
```Python
--8<-- "laboratory_work_2/racing/racing/settings.py:33:41"
```

- Поменяем часовой пояс на GMT+3:
```Python
--8<-- "laboratory_work_2/racing/racing/settings.py:109:109"
```

- Поменяем `LOGIN_REDIRECT_URL` (используется для декоратора `login_required` и дефолтного view `django.contrib.auth.views.login`):
```Python
--8<-- "laboratory_work_2/racing/racing/settings.py:126:126"
```