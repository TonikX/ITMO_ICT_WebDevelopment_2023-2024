from django.urls import path
from .views import *

urlpatterns = [
    path('readers/list/', ReaderListAPIView.as_view()),
    path('readers/create/', CreateReaderAPIView.as_view()),
    path('readers/<int:pk>/', ReaderDetailAPIView.as_view()),
    path('books/list/', BookListAPIView.as_view()),
    path('books/create/', CreateBookAPIView.as_view()),
    path('books/<int:pk>/', OneBookAPIView.as_view()),
    path('book-instance/list/', BookInstanceAPIView.as_view()),
    path('book-instance/create/', CreateInstanceAPIView.as_view()),
    path('book-instance/<int:pk>/', OneInstanceAPIView.as_view()),
    path('rooms/list/', RoomListAPIView.as_view()),
    path('readers-info/', ReaderInfoAPIView.as_view()),
    path('take_book/', BookTakingAPIView.as_view()),
    path('taking_book/',BookTaking2APIView.as_view()),


]