# Представления

Представления — основная логика нашего сайта. В файле `views.py` пропишем необходимые функции.

=== "Регистрация, вход и выход"

    ```Python
    from django.shortcuts import render, redirect
    from django.contrib import messages
    from django.contrib.auth import authenticate, login, logout
    from django.contrib.auth.forms import AuthenticationForm
    from .forms import NewUserForm


    --8<-- "laboratory_work_2/hotelProject/hotel_app/views.py:49:86"
    ```

=== "Списковые и детальные отображения"

    ```Python
    from django.shortcuts import render, redirect
    from hotel_app.models import Hotel, Room
    from django.views.generic.list import ListView
    from django.views.generic.detail import DetailView


    --8<-- "laboratory_work_2/hotelProject/hotel_app/views.py:87:128"
    ```

=== "Бронирование"

    ```Python
    from django.shortcuts import render, redirect
    from hotel_app.models import Room, Booking
    from .forms import BookRoomForm


    --8<-- "laboratory_work_2/hotelProject/hotel_app/views.py:27:48"
    ```

=== "Оставление отзыва"

    ```Python
    from django.shortcuts import render, redirect
    from hotel_app.models import Room, Comment
    from .forms import ReviewForm


    --8<-- "laboratory_work_2/hotelProject/hotel_app/views.py:11:27"
    ```
