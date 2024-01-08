from django.contrib import admin
from django.urls import path, include
from django.conf import settings

handler404 = 'journal.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('journal.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
] 

