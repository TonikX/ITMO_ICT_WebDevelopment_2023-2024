# book_exchange/serializers.py
from rest_framework import serializers
from .models import Book, UserProfile, Review, BookList, BookClub, ClubMembership, ClubPost, Comment

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookList
        fields = '__all__'

class BookClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookClub
        fields = '__all__'

class ClubMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubMembership
        fields = '__all__'

class ClubPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubPost
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
