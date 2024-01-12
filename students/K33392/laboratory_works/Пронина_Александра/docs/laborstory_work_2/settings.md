# Создание проекта

Установим фреймворк Django и библиотеку django-bootstrap5, которая нам понадобится для удобного форматирования форм:


    pip install django django_bootstrap5


Создадим проект `hotel_site` и приложение `hotels`:

    django-admin startproject hotel_site
    cd hotel_site
    python manage.py startapp hotel


Перейдём в файл `settings.py` и сделаем некоторые изменения:

Добавим созданное приложение и bootstrap5 в `INSTALLED_APPS`:



`