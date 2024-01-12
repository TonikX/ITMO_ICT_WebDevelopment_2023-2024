from rest_framework import serializers
from .models import *


class MuseumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Museum
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Card
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    card = CardSerializer()

    class Meta:
        model = Item
        fields = '__all__'


class FoundationSerializer(serializers.ModelSerializer):
    museum = MuseumSerializer()
    card = CardSerializer(many=True)

    class Meta:
        model = Foundation
        fields = '__all__'


class ExhibitionSerializer(serializers.ModelSerializer):
    museum = MuseumSerializer()
    item = ItemSerializer(many=True)

    class Meta:
        model = Exhibition
        fields = '__all__'


class ItemToExhibitionSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    exhibition = ExhibitionSerializer()

    class Meta:
        model = ItemToExhibition
        fields = '__all__'


class CardToFoundationSerializer(serializers.ModelSerializer):
    card = CardSerializer()
    foundation = FoundationSerializer()

    class Meta:
        model = CardToFoundation
        fields = '__all__'


class ItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class CardCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'


class ItemToExhibitionCreateSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    exhibition = ExhibitionSerializer()

    class Meta:
        model = ItemToExhibition
        fields = ['id', 'item', 'exhibition', 'send_date', 'return_date']


class CardToFoundationCreateSerializer(serializers.ModelSerializer):
    card = CardSerializer()
    foundation = FoundationSerializer()

    class Meta:
        model = CardToFoundation
        fields = ['id', 'set', 'foundation', 'send_date', 'return_date']


class FoundationExhibitionSerializer(serializers.ModelSerializer):
    num_exhibitions = serializers.IntegerField()

    class Meta:
        model = Foundation
        fields = ['id', 'name', 'num_exhibitions']


class CardItemSerializer(serializers.ModelSerializer):
    num_items = serializers.IntegerField()

    class Meta:
        model = Foundation
        fields = ['id', 'name', 'num_items']


class FoundationRatioSerializer(serializers.ModelSerializer):
    percentage = serializers.IntegerField()

    class Meta:
        model = Foundation
        fields = ['id', 'name', 'percentage']


class ItemCommonExhibitionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name', 'exhibition']
