from rest_framework import serializers

from .models import Newspaper, PrintingHouse, Editor, PrintRun, PostOffice, PostalArrival


class NewspaperSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Newspaper.
    """

    class Meta:
        model = Newspaper
        fields = ['id', 'name', 'edition_index', 'editor', 'price_per_copy']


class PrintingHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintingHouse
        fields = '__all__'


class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = '__all__'


class PrintRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintRun
        fields = '__all__'


class PostOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostOffice
        fields = '__all__'


class PostalArrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalArrival
        fields = '__all__'
