from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorList.as_view()),
   path('warrior/create/', WarriorCreate.as_view()),
   path('professions/', ProfessionList.as_view()),
   path('profession/create/', ProfessionCreate.as_view()),
   path('profession/detail/<int:pk>', ProfessionDetail.as_view()),
]