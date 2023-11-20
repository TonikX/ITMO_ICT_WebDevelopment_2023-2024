# admin.py

 В данном коде:

    from django.contrib import admin - подключается модуль административной панели Django.
    from .models import Tour, Reservation, Review - импортируются модели Tour, Reservation и Review из текущего приложения.

Затем с помощью admin.site.register() эти модели регистрируются в административной панели Django. Это делается для того, чтобы вы могли управлять данными этих моделей через веб-интерфейс административной панели Django.

Этот код нужен для настройки административной части вашего веб-приложения Django, где вы сможете управлять данными о турах (Tour), бронированиях (Reservation) и отзывах (Review).

```python
from django.contrib import admin
from .models import Tour, Reservation, Review

admin.site.register(Tour)
admin.site.register(Reservation)
admin.site.register(Review)
```
