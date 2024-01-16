from rest_framework.routers import SimpleRouter
from . import views
from django.urls import path, include


router = SimpleRouter()
router.register('animals', views.AnimalViewSet)
router.register('winter-places', views.WinterPlaceViewSet)

router.register('food', views.TypeOfDietViewSet)
router.register('diets', views.DietViewSet)
router.register('habitats', views.HabitatViewSet)

router.register('locations', views.AreaViewSet)
router.register('aviaries', views.AviaryViewSet)
router.register('who-is-there', views.AnimalInAviaryViewSet)

router.register('workers', views.WorkerViewSet)
router.register('other-zoos', views.ZooViewSet)
router.register('ownings', views.OwningViewSet)

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('change-password/<int:pk>/', views.ChangePasswordView.as_view(), name='change-password'),

    path('', include(router.urls)),
]
