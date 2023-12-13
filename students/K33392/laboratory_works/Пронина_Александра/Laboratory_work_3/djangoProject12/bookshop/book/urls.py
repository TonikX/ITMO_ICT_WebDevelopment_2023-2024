from django.contrib.auth.views import *
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import BookListView, RegisterView, LoginView, CartView, ReviewView, FavoritesView, BookViewSet, \
    BookDetailView

router = DefaultRouter()
router.register(r'books', BookListView, basename='book')
router.register(r'book', BookViewSet)
#router.register(r'update', BookDetailView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('cart/', CartView.as_view(), name='cart'),
    path('reviews/', ReviewView.as_view(), name='reviews'),
    path('favorites/', FavoritesView.as_view(), name='favorites'),#Маршрут для страницы избранного.
    path('', include(router.urls)),
]
