# Ссылки

### Импорты

```
from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path, include

```

### Регистрация адресов

```
router = SimpleRouter()

router.register('newspaper', views.NewspaperViewSet)
router.register('printer', views.PrinterViewSet)
router.register('post-office', views.PostOfficeViewSet)
router.register('printing-newspapers', views.PrintingNewspaperViewSet)
router.register('ordering-newspapers', views.PostOfficeOrderViewSet)
router.register('transporting', views.TransportationViewSet)

router.register('do', views.ActionViewSet, basename='action')

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('change-password/<int:pk>/', views.ChangePasswordView.as_view(), name='change-password'),

    path('', include(router.urls)),
]

```