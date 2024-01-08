from django.urls import path
from .views import *


app_name = "beauty_marketplace_app"


urlpatterns = [
   path('salons/', SalonListAPIView.as_view()),
   path('salons/<int:pk>', SalonRetrieveAPIView.as_view()),
   path('salons/create/', SalonCreateAPIView.as_view()),

   path('owners/', SalonOwnerListAPIView.as_view()),
   path('owners/create/', SalonOwnerCreateAPIView.as_view()),

   path('services/', SalonServiceListAPIView.as_view()),
   path('services/<int:pk>', SalonServiceRetrieveAPIView.as_view()),
   path('<int:salon_id>/services/', SalonServiceListAPIView.as_view(), name='salon_services'),

   path('services/create/', SalonServiceCreateAPIView.as_view()),

   path('customers/', CustomerListAPIView.as_view()),
   path('customers/<int:pk>', CustomerRetrieveAPIView.as_view()),
   path('customers/create/', CustomerCreateAPIView.as_view()),

   path('appointments/', SalonAppointmentListAPIView.as_view()),
   path('appointments/<int:pk>', SalonAppointmentRetrieveAPIView.as_view()),
   path('appointments/<int:pk>/edit/', SalonAppointmentUpdateAPIView.as_view()),

   path('appointments/create/', SalonAppointmentCreateAPIView.as_view()),


   path('salons/comments/', SalonCommentsListAPIView.as_view()),
   path('salons/comments/<int:pk>', SalonCommentsRetrieveAPIView.as_view()),
   path('salons/comments/create', SalonCommentsCreateAPIView.as_view()),

   path('services/comments/', SalonServiceCommentsListAPIView.as_view()),
   path('services/comments/<int:pk>', SalonServiceCommentsRetrieveAPIView.as_view()),
   path('services/comments/create/', SalonServiceCommentsCreateAPIView.as_view()),

   path('api/current_user/', current_user),
   path('api/login/', login_view)

]
