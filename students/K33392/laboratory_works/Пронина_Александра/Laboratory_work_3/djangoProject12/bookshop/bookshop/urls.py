from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),  # Основные маршруты проекта
    path('auth/', include('djoser.urls')),  # URL-маршруты для djoser
    path('auth-token/', include('djoser.urls.authtoken')),  # Другой URL для авторизации по токену
    path('auth-jwt/', include('djoser.urls.jwt')),
]
