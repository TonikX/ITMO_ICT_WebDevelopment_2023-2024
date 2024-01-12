# Админ-панель

     # Импорт модуля admin из приложения django.contrib.
    from django.contrib import admin
    
    # Импорт моделей Hotel, Reservation, Room и Comment из текущего приложения (.models).
    from .models import Hotel, Reservation, Room, Comment
    
    # Регистрация моделей в административном интерфейсе Django.
    admin.site.register(Hotel)        # Регистрация модели Hotel.
    admin.site.register(Reservation)  # Регистрация модели Reservation.
    admin.site.register(Room)         # Регистрация модели Room.
    admin.site.register(Comment)      # Регистрация модели Comment.

Однако прежде чем добавлять в админ палени модели нужно их создать