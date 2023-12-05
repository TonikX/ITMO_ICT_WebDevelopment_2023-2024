"""
URL configuration for NewspaperDistributionSystem project.

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
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from distribution.views import (
    NewspaperListCreateView,
    NewspaperRetrieveUpdateDestroyView,
    PrintingHouseListCreateView,
    PrintingHouseRetrieveUpdateDestroyView, EditorListCreateView, EditorRetrieveUpdateDestroyView,
    PrintRunListCreateView, PrintRunRetrieveUpdateDestroyView, PostOfficeListCreateView,
    PostOfficeRetrieveUpdateDestroyView, PostalArrivalListCreateView, PostalArrivalRetrieveUpdateDestroyView,
    PrintingHouseAddressesView,
    MaxPrintRunEditorView, PostOfficeAddressesView, UnderstockedNewspapersView, NewspaperArrivalView)

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v2',
        description="Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hardbeat34@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('newspapers/', NewspaperListCreateView.as_view(), name='newspaper-list-create'),
    path('newspapers/<int:pk>/', NewspaperRetrieveUpdateDestroyView.as_view(),
         name='newspaper-retrieve-update-destroy'),

    path('printinghouses/', PrintingHouseListCreateView.as_view(), name='printinghouse-list-create'),
    path('printinghouses/<int:pk>/', PrintingHouseRetrieveUpdateDestroyView.as_view(),
         name='printinghouse-retrieve-update-destroy'),

    path('editors/', EditorListCreateView.as_view(), name='editor-list-create'),
    path('editors/<int:pk>/', EditorRetrieveUpdateDestroyView.as_view(), name='editor-retrieve-update-destroy'),

    path('printruns/', PrintRunListCreateView.as_view(), name='printrun-list-create'),
    path('printruns/<int:pk>/', PrintRunRetrieveUpdateDestroyView.as_view(), name='printrun-retrieve-update-destroy'),

    path('postoffices/', PostOfficeListCreateView.as_view(), name='postoffice-list-create'),
    path('postoffices/<int:pk>/', PostOfficeRetrieveUpdateDestroyView.as_view(),
         name='postoffice-retrieve-update-destroy'),

    path('postalarrivals/', PostalArrivalListCreateView.as_view(), name='postalarrival-list-create'),
    path('postalarrivals/<int:pk>/', PostalArrivalRetrieveUpdateDestroyView.as_view(),
         name='postalarrival-retrieve-update-destroy'),

    # -------------------------------------------------------------------------------------------------------------------

    path('newspapers/printing-houses/', PrintingHouseAddressesView.as_view(), name='printing_house_addresses'),
    path('max_print_run_editor/', MaxPrintRunEditorView.as_view(), name='max_print_run_editor'),

    path('newspapers/price-greater/', PostOfficeAddressesView.as_view(), name='newspaper-price-greater-post-offices'),
    path('newspapers/copies-less-than/', UnderstockedNewspapersView.as_view(),
         name='newspaper-copies-less-destinations'),
    path('newspaper_arrival/', NewspaperArrivalView.as_view(), name='newspaper_arrival'),

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')

]
