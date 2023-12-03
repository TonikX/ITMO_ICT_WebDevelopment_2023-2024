from rest_framework import serializers
from .models import Profile, Book, ExchangeRequest


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ["id", "username", "first_name", "last_name", "phone_number", "email", "birth_date", "location"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookDepthSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer()

    class Meta:
        model = Book
        fields = "__all__"
        depth = 1


class ExchangeRequestSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ExchangeRequest
        fields = "__all__"


class ExchangeRequestDepthSerializer(serializers.ModelSerializer):    
    to_user = ProfileSerializer()
    book_offered = BookDepthSerializer()

    class Meta:
        model = ExchangeRequest
        fields = "__all__"
        depth = 2


class ExchangeRequestStatusSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ExchangeRequest
        fields = ["status"]
