# Настройка окружения
Создадим проект средствами PyCharm Professional Edition. В нём используется версия Django 4.2, интерпретатор Python 3.11.2. Все необходимые папки и файлы уже созданы.

В соответствии с заданием требуется использовать СУБД PostgreSQL 16. Для этого изменим переменную DATABASES в файле settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
## Сущности базы данных

Для реализации задания нам потребуются следующие сущности:

* Hotel
* Customer
* Room
* Booking
* Review

Более подробная информация и реализация представлены в файле models.py и на соответствующей странице отчёта.

Зарегистрируем эти сущности в файле admin.py:
```python
from django.contrib import admin

from .models import *

admin.site.register(Hotel)
admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Review)
```
Для регистрации прежде всего необходимо создать формы. Для этого создадим файл forms.py . Для создания пользователя будем использовать уже встроенный класс User, который предоставляет необходимый функционал (никнейм, пароль, почта, встроенная система авторизации). Код форм представлен на соответствующей странице отчёта.

Далее создадим файл views.py и реализуем в нём функции для регистрации. Также реализуем HTML-страницы, которые по нашим представлениям и формам будет собирать страницу регистрации для обычного пользователя. Код представлен на соответствующей странице отчёта.

Аналогичные действия сделаем для страницы авторизации. Стоит заметить, что Django предоставляет готовое представление для страницы входа, поэтому зде
сь достаточно создать HTML-страницу и добавить ссылку на неё в urls.py.

## Регистрация новых пользователей:
Для этого создано представление registerPage в файле views.py. Пользователь заполняет форму регистрации, после че
го его данные сохраняются в базе данных, а также создается запись в таблице Customer, связанной с моделью User из стандар
тной библиотеки Django. При успешной регистрации пользователь перенаправляется на страницу входа.
```python
def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Создание объекта Customer после регистрации пользователя
            Customer.objects.create(
                user=User.objects.get(username=form.cleaned_data.get('username')),
                name=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
            )
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'hotels/register.html', {'form': form})

```

## Просмотр и резервирование номеров:
Для просмотра номеров создано представление hotelpage, которое отображает страницу отдельного отеля с его номерами и отзывами. Для р
езервирования номера используется представление booking, которое обрабатывает запросы на бронирование, создавая новую запись в таблице Booking базы данных.
```python
def hotelpage(request, hotel_name):
    # Загрузка объекта отеля из базы данных
    hotel = get_object_or_404(Hotel, name=hotel_name)
    # Загрузка списка номеров отеля
    rooms = Room.objects.filter(hotel=hotel)
    # Отображение страницы отеля с номерами
    return render(request, 'hotels/hotelpage.html', context)

def booking(request, hotel_name, room_category):
    # Загрузка объекта отеля и номера для бронирования
    hotel = get_object_or_404(Hotel, name=hotel_name)
    room = get_object_or_404(Room, hotel=hotel, category=room_category)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user.customer
            booking.room = room
            booking.status = 'Pending'
            booking.save()
            return redirect('profile')
    else:
        form = BookingForm(initial={'user': request.user.customer, 'room': room, 'check_in_date': datetime.date.today(), 'check_out_date': datetime.date.today() + datetime.timedelta(days=1)})
    return render(request, 'hotels/booking.html', {'room': room, 'form': form})

```

## Написание отзывов к номерам:
Пользователи могут добавлять отзывы к номерам с помощью представления review. После добавления отзыва создается новая запись в таблице Review с данными 
о комментаторе, рейтинге, тексте комментария и периоде проживания.
```python
def review(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user.customer)
    review = Review.objects.filter(booking=booking).first()
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.booking = booking
            review.user = request.user.customer
            review.save()
            return redirect('profile')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'hotels/review.html', {'form': form, 'booking': booking, 'review': review})

```

## Администрирование пользователей и их заселение/выселение:
Администратор может управлять пользователями и их бронированиями через Django-admin. Для этого администратор может использовать встроенные
возможности Django-admin, такие как создание, редактирование и удаление записей из таблиц базы данных.

## Завершение работы
По завершении работы необходимо добавить все маршруты в файл urls.py и проверить работоспособность сайта. Содержимое файла:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name='home'),
    path('hotels/', views.hotels, name='hotels'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('hotelpage/<str:hotel_name>/', views.hotelpage, name='hotelpage'),
    path('booking/<str:hotel_name>/<str:room_category>/', views.booking, name='booking'),
    path('editbooking/<str:booking_id>/', views.edit_booking, name='edit_booking'),
    path('cancelbooking/<str:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('review/<str:booking_id>/', views.review, name='review'),
]
```