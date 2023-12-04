from rest_framework import serializers
from .models import Museum, Author, Set, Item, Foundation, Exhibition, ItemToExhibition, SetToFoundation


class MuseumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museum
        fields = ['id', 'name', 'address', 'director']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'country']


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ['id', 'name', 'author']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'inventory_number', 'set', 'author', 'creation_date', 'is_date_exact',
                  'country', 'description', 'image']


class FoundationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foundation
        fields = ['id', 'name', 'address', 'museum', 'curator', 'set']


class ExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = ['id', 'name', 'museum', 'description', 'contact_name', 'contact_phone', 'address', 'open_date',
                  'close_date']


class ItemToExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemToExhibition
        fields = ['id', 'item', 'exhibition', 'send_date', 'return_date', 'director_signature', 'curator_signature']


class SetToFoundationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetToFoundation
        fields = ['id', 'set', 'foundation', 'send_date', 'return_date', 'director_signature', 'curator_signature']
