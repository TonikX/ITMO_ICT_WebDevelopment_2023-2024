from . import views
from django.urls import path, include
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register('profile', viewset=views.ProfileViewSet)
router.register('product', viewset=views.ProductViewSet)
router.register('eaten', viewset=views.EatenViewSet)
router.register('calculator', viewset=views.CountViewSet, basename='calculator')


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('change-password/<int:pk>/', views.ChangePasswordView.as_view(), name='change-password'),

    path('', include(router.urls)),
]
