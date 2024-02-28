from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [

    path('books/all/', BookListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookRetrieveView.as_view(), name='books_detail'),
    path('books/create/', BookCreateView.as_view(), name='books_create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='books_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='books_delete'),

    path('halls/all/', HallListView.as_view(), name='halls_list'),
    path('halls/<int:pk>/', HallRetrieveView.as_view(), name='halls_detail'),
    path('halls/create/', HallCreateView.as_view(), name='halls_create'),
    path('halls/update/<int:pk>/', HallUpdateView.as_view(), name='halls_update'),
    path('halls/delete/<int:pk>/', HallDeleteView.as_view(), name='halls_delete'),

    path('readers/all/', ReaderListView.as_view(), name='readers_list'),
    path('readers/<int:pk>/', ReaderRetrieveView.as_view(), name='readers_detail'),
    path('readers/create/', ReaderCreateView.as_view(), name='readers_create'),
    path('readers/update/<int:pk>/', ReaderUpdateView.as_view(), name='readers_update'),
    path('readers/delete/<int:pk>/', ReaderDeleteView.as_view(), name='readers_delete'),

    path('ownerships/all/', OwnershipListView.as_view(), name='ownerships_list'),
    path('ownerships/<int:pk>/', OwnershipRetrieveView.as_view(), name='ownerships_detail'),
    path('ownerships/create/', OwnershipCreateView.as_view(), name='ownerships_create'),
    path('ownerships/update/<int:pk>/', OwnershipUpdateView.as_view(), name='ownerships_update'),
    path('ownerships/delete/<int:pk>/', OwnershipDeleteView.as_view(), name='ownerships_delete'),

    path('availabilities/all/', AvailabilityListView.as_view(), name='availabilities_list'),
    path('availabilities/<int:pk>/', AvailabilityRetrieveView.as_view(), name='availabilities_detail'),
    path('availabilities/create/', AvailabilityCreateView.as_view(), name='availabilities_create'),
    path('availabilities/update/<int:pk>/', AvailabilityUpdateView.as_view(), name='availabilities_update'),
    path('availabilities/delete/<int:pk>/', AvailabilityDeleteView.as_view(), name='availabilities_delete'),

    path('good_book/<int:pk>/', GoodBookRetrieveView.as_view(), name='good_book'),
    path('available_books/<int:reader>/', AvailableBooks.as_view(), name='available_books'),

    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),
    path('logout', LogOut.as_view()),
]