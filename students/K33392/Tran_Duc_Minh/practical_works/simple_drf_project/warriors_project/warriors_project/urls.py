from django.contrib import admin
from django.urls import path, include

from warriors_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('war/', include('warriors_app.urls', namespace='warriors')),
     path('pro/', include('warriors_app.urls', namespace='professions')),
    path('profession/create/', views.ProfessionCreateView.as_view()),
]



