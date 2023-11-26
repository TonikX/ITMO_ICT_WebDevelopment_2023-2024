# book_exchange/views.py
from rest_framework import viewsets
from .models import Book, UserProfile, Review, BookList, BookClub, ClubMembership, ClubPost, Comment
from .serializers import BookSerializer, UserProfileSerializer, ReviewSerializer, BookListSerializer, \
    BookClubSerializer, ClubMembershipSerializer, ClubPostSerializer, CommentSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class BookListViewSet(viewsets.ModelViewSet):
    queryset = BookList.objects.all()
    serializer_class = BookListSerializer

class BookClubViewSet(viewsets.ModelViewSet):
    queryset = BookClub.objects.all()
    serializer_class = BookClubSerializer

class ClubMembershipViewSet(viewsets.ModelViewSet):
    queryset = ClubMembership.objects.all()
    serializer_class = ClubMembershipSerializer

class ClubPostViewSet(viewsets.ModelViewSet):
    queryset = ClubPost.objects.all()
    serializer_class = ClubPostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
