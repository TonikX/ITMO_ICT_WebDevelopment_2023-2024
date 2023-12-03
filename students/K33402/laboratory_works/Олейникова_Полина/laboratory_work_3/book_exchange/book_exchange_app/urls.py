from django.urls import path
from rest_framework import routers
from .views import *

app_name = "book_exchange_app"

router = routers.DefaultRouter()

urlpatterns = [
    path('books/', GetBooks.as_view(), name='books'),
    path('books/own/', GetOwnBooks.as_view(), name='own_books'),
    path('books/<int:pk>/', GetBook.as_view(), name='book'),
    path('books/create/', CreateBook.as_view(), name='create_book'),
    path('books/<int:pk>/update/', UpdateBook.as_view(), name='update_book'),
    path('books/<int:pk>/delete/', DeleteBook.as_view(), name='delete_book'),

    path('requests/from/', GetExchangeRequestsFrom.as_view(), name='requests_from'),
    path('requests/to/', GetExchangeRequestsTo.as_view(), name='requests_to'),
    path('requests/<int:pk>/', GetExchangeRequest.as_view(), name='request'),
    path('requests/create/', CreateExchangeRequest.as_view(), name='create_request'),
    path('requests/<int:pk>/update/', UpdateExchangeRequest.as_view(), name='update_request'),
    
    path('books/<int:pk>/dates/', GetBookDates.as_view(), name='get_book_dates'),
]