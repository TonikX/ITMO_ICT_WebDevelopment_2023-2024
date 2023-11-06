from django.urls import path
from . import views

urlpatterns = [
    # Добавить URL-маршрут для отображения информации о владельце
    path('owner/<int:owner_id>/', views.owner_detail, name='owner_detail'),
]
