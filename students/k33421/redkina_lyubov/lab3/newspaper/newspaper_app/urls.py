from django.urls import path
from .views import (
    NewspaperListCreateView, NewspaperDetailView,
    PrintingHouseListCreateView, PrintingHouseDetailView,
    PostOfficeListCreateView, PostOfficeDetailView,
    NewspaperPrintListCreateView, NewspaperPrintDetailView,
    NewspaperArrivalListCreateView, NewspaperArrivalDetailView,
    NewspaperOrderListCreateView, NewspaperOrderDetailView,
    UserProfileListCreateView, UserProfileDetailView,
)

urlpatterns = [
    path('newspapers/', NewspaperListCreateView.as_view(), name='newspaper-list-create'),
    path('newspapers/<int:pk>/', NewspaperDetailView.as_view(), name='newspaper-detail'),

    path('printinghouses/', PrintingHouseListCreateView.as_view(), name='printinghouse-list-create'),
    path('printinghouses/<int:pk>/', PrintingHouseDetailView.as_view(), name='printinghouse-detail'),

    path('postoffices/', PostOfficeListCreateView.as_view(), name='postoffice-list-create'),
    path('postoffices/<int:pk>/', PostOfficeDetailView.as_view(), name='postoffice-detail'),

    path('newspaperprints/', NewspaperPrintListCreateView.as_view(), name='newspaperprint-list-create'),
    path('newspaperprints/<int:pk>/', NewspaperPrintDetailView.as_view(), name='newspaperprint-detail'),

    path('newspaperarrivals/', NewspaperArrivalListCreateView.as_view(), name='newspaperarrival-list-create'),
    path('newspaperarrivals/<int:pk>/', NewspaperArrivalDetailView.as_view(), name='newspaperarrival-detail'),

    path('newspaperorders/', NewspaperOrderListCreateView.as_view(), name='newspaperorder-list-create'),
    path('newspaperorders/<int:pk>/', NewspaperOrderDetailView.as_view(), name='newspaperorder-detail'),

    path('userprofiles/', UserProfileListCreateView.as_view(), name='userprofile-list-create'),
    path('userprofiles/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
]
