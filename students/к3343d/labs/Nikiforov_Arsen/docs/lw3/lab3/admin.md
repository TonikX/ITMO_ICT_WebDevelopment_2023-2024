### admin.py


# Обзор admin.py

В файле `admin.py` определяются настройки административного интерфейса Django для наших моделей. Это включает в себя регистрацию моделей, чтобы они были доступны в админ-панели, а также настройку форм и интерфейсов для управления данными моделей.

## Импорты

```python
from django.contrib import admin
from django import forms
from .models import Room, Client, ClientInfo, Employee, Floor, Day, EmployeeFloor, EmployeeDay
from .models import CustomUser
```

Здесь мы импортируем необходимые модули и модели. `admin` и `forms` используются для настройки административного интерфейса и форм.

## Настройка формы для модели Room

```python
class RoomAdminForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'room_type': forms.Select(choices=Room.ROOM_TYPES)
        }
```

Этот класс определяет форму для модели `Room`. Мы указываем, что хотим использовать все поля (`fields = '__all__'`) и настраиваем виджет для поля `room_type`.

## Регистрация моделей

```python
class RoomAdmin(admin.ModelAdmin):
    form = RoomAdminForm
    
admin.site.register(CustomUser)
admin.site.register(Room, RoomAdmin)
admin.site.register(Client)
admin.site.register(ClientInfo)
admin.site.register(Employee)
admin.site.register(Floor)
admin.site.register(Day)
admin.site.register(EmployeeFloor)
admin.site.register(EmployeeDay)
```

Здесь мы регистрируем наши модели в админке Django. Для модели `Room` используется специально настроенная форма `RoomAdminForm`.

