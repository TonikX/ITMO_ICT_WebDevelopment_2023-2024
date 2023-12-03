# Serializers

## ProfileSerializer
```
class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ["id", "first_name", "last_name", "phone_number", "email", "birth_date", "location"]
```
## BookSerializer
```
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
```
## BookDepthSerializer
```
class BookDepthSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer()

    class Meta:
        model = Book
        fields = "__all__"
        depth = 1
```
## ExchangeRequestSerializer
```
class ExchangeRequestSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ExchangeRequest
        fields = "__all__"
```
## ExchangeRequestDepthSerializer
```
class ExchangeRequestDepthSerializer(serializers.ModelSerializer):    
    to_user = ProfileSerializer()
    book_offered = BookDepthSerializer()

    class Meta:
        model = ExchangeRequest
        fields = "__all__"
        depth = 2
```
## ExchangeRequestStatusSerializer
```
class ExchangeRequestStatusSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ExchangeRequest
        fields = ["status"]
```