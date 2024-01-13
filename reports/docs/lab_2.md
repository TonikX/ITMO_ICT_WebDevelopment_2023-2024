#Описание моделей
___
<br>

##*Hotel (Отели)*
<br>

Модель ***Hotel*** представляет отель и содержит следующие поля: <br>
- **name (название):** CharField с максимальной длиной 200 символов, используется для хранения названия 
отеля. <br/>
- **address (адрес):** CharField с максимальной 
длиной 200 символов, используется для хранения адреса отеля. <br/>
- **website (вебсайт):** CharField с максимальной 
длиной 200 символов, используется для хранения вебсайта отеля. <br/>
- **phone (тел.номер):** PhoneNumberField, используется 
для хранения телефонного номера отеля. <br/>
- **owner (владелец):** CharField с максимальной длиной 200 символов, используется 
для хранения информации о владельце отеля. <br/>
- **rating (рейтинг):**  FloatField, используется для хранения рейтинга отеля.<br/>
- **small_description (краткое описание):** CharField с максимальной длиной 400 символов, используется 
для хранения краткого описания отеля. <br/>
- **full_description (подробное описание):** TextField, используется 
для хранения подробного описания отеля. <br/>
- **image (картинка):**  ImageField, используется для хранения фотографии отеля. <br/>
- **date_created (дата создания):**  DateTimeField, используется для хранения информации о дате добавления отеля.
<br><br>

##*Room(номера)*
<br>
Модель ***Room*** представляет отель и содержит следующие поля: <br/>
- **hotel (отель):** ForeignKey с ссылкой на модель *Hotel*, используется для связи номера с соответствующим отелем <br/>
- **category (категория):** CharField с максимальной длиной 200 символов, используется 
для хранения информации о категории номера. <br/>
- **price (стоимость):** FloatField, используется 
для хранения информации о стоимости номера. <br/>
- **amenities (удобства):** TextField, используется 
для хранения информации о удобствах, предоставляемых в номере. <br/>
- **image (картинка):**  ImageField, используется для хранения фотографии номера. <br/>
- **date_created (дата создания):**  DateTimeField, используется для хранения информации о дате добавления номера.
<br><br>

##*Customer(посетители)*
<br>

Модель ***Customer*** представляет отель и содержит следующие поля: <br/>
- **user (пользователь):**  OneToOneField с ассоциацией с *User*, используется для хранения информации о посетителе. <br/>
- **name (имя):** CharField с максимальной длиной 200 символов, используется 
для хранения имени посетителе. <br/>
- **email:** CharField с максимальной длиной 200 символов, используется 
для хранения электронной почты посетителя. <br/>
- **phone (тел.номер):** CharField с максимальной длиной 200 символов, используется 
для хранения телефонного номера отеля. <br/>
- **image (картинка):**  ImageField, используется для хранения фотографии номера. <br/>
- **date_registered (дата создания):**  DateTimeField, используется для хранения информации о дате регистации посетителя.
<br><br>

##*Booking(бронирования)*
<br>

Модель ***Booking*** представляет бронирование и содержит следующие поля: <br/>
- **user (пользователь):** ForeignKey с ссылкой на модель *Customer*, используется для связи брони с соответствующим пользователем <br/>
- **room (номер):** ForeignKey с ссылкой на модель *Room*, используется для связи брони с соответствующим номером <br/>
- **status (статус):** CharField с максимальной длиной 200 символов, используется 
для хранения статуса бронирования. <br/>
- **check_in_date (дата заселения):**  DateTimeField, используется для хранения информации о дате заселения.
- **check_out_date (дата выселения):**  DateTimeField, используется для хранения информации о дате выселения.
<br><br>

##*Review(отзывы)*
<br>

- **booking (пользователь):**  OneToOneField с ассоциацией с *Booking*, используется для хранения информации о бронировании. <br/>
- **rating (рейтинг):** PositiveIntegerField, используется для хранения оценки. <br/>
- **comment (комментарий):** TextField, используется для хранения текста отзыва. <br/>
- **date_created (дата создания):**  DateTimeField, используется для хранения информации о дате добавления отзыва.

#*Формы*
___
<br/>

##*BookingForm*
<br/>

Класс **BookingForm** является формой для модели **Booking**. <br/>
Он наследует от **ModelForm** и определяет следующие поля: <br/>
- **check_in_date** (дата заселения) <br/>
- **check_in_date** (дата выселения) <br/>
<br><br>
##*EditBookingForm*
<br/>

Класс **EditBookingForm** является формой для модели **Booking**. <br/>
Он наследует от **forms.ModelForm** и определяет следующие поля: <br/>
- **check_in_date** (дата заселения) <br/>
- **check_in_date** (дата выселения) <br/>
<br><br>


##*CreateUserForm*
<br/>

Класс **CreateUserForm** является формой для модели **User**. <br/>
Он наследует от **UserCreationForm** и определяет следующие поля: <br/>
- **username** <br/>
- **email** <br/>
- **password1** <br/>
- **password2** <br/>
<br><br>

##*CustomerForm*
<br/>

Класс **CustomerForm** является формой для модели **Customer**. <br/>
Он наследует от **ModelForm** и определяет следующие поля: <br/>
- **name** (имя): <br/>
- **email:** <br/>
- **phone** (тел.номер): <br/>
- **image** (картинка): <br/>
- **date_registered** (дата создания):<br/>
<br><br>

##*ReviewForm*
<br/>

Класс **ReviewForm** является формой для модели **Review**. <br/>
Он наследует от **ModelForm** и определяет следующие поля: <br/>
- **rating** (рейтинг)<br/>
- **comment** (комментарий)<br/>
- **date_created** (дата создания)
<br><br>

#Роутер
<br/>

##lab2/urls.py
<br/>

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotels.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
<br/>

##hotels/urls.py
<br/>

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