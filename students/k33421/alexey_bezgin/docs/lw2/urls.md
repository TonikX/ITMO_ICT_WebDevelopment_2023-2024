# Конфигурация адресации

Осталось опеределить адреса для функций, описанных в предыдущем разделе.

Импортировав в ```urls.py``` проекта все необходимые ```views``` можем задать следующую адресацию:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('personal_space/', personal_space_view),
    path('user_reservations/', show_user_reservations, name='user_reservations'),
    path('edit_reservation/<int:reservation_id>/', edit_reservation, name='edit_reservation'),
    path('delete_reservation/<int:reservation_id>/', delete_reservation, name='delete_reservation'),
    path('flight_passengers/<int:flight_id>/', flight_passengers, name='flight_passengers'),
    path('personal_space/create_review/<int:flight_id>/', create_review, name='create_review'),
    path('flight_reviews/<int:flight_id>/', flight_reviews, name='flight_reviews'),
    path('all_flights', flights_list, name="flights_list"),
    path('', home, name='home'),
]
```