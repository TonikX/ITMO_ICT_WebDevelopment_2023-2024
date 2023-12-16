"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import tour_list_view, tour_detail_view, agency_detail_view, reservation_detail_view, review_detail_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tour_list_view, name='home'),
    path('tour/', tour_list_view, name='tour_list'),
    path('tour/<int:pk>/', tour_detail_view, name='tour_detail'),
    path('agency/<int:pk>/', agency_detail_view, name='agency_detail'),
    path('reservation/<int:pk>/', reservation_detail_view, name='reservation_detail'),
    path('review/<int:pk>/', review_detail_view, name='review_detail'),
]








