from django.urls import path
from LR1_secondApp.views import *

urlpatterns = [
    path('Disks/', DisksS.as_view()),
    path('Disks/<int:pk>', DisksS.as_view()),
    path('Games/', GamesS.as_view()),
    path('Games/<int:pk>', GamesS.as_view()),
    path('Sale/', SaleS.as_view()),
    path('Sale/<int:pk>', SaleS.as_view()),
    path('Admission/', AdmissionS.as_view()),
    path('Admission/<int:pk>', AdmissionS.as_view()),
    path('Sale_point/', Sale_pointS.as_view()),
    path('Admission_point/', Admission_pointS.as_view()),
]
