from django.urls import path
from django.contrib.auth.views import auth_logout, auth_login
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('TytTour/main', index),
    path('TytTour/registration/', CreatePersonView),
    path('TytTour/login/', LoginPerson),
    path('TytTour/logout/', login_required(LogoutPerson)),
    path('TytTour/order/<int:tour_id>', login_required(booking)),
    path('TytTour/order/update/<int:pk>', login_required(bookUpdate.as_view())),
    path('TytTour/order/delete/<int:pk>', login_required(bookDelete.as_view())),
    path('TytTour/profile/<int:pk>', login_required(userProfile.as_view())),
    path('TytTour/profile/<int:pk>/update/', login_required(userProfileUpdate.as_view())),
    path('TytTour/tourinfo/<int:pk>', login_required(tourDetail.as_view())),
    path('TytTour/comment/create/<int:pk>', login_required(createComment.as_view())),
]
