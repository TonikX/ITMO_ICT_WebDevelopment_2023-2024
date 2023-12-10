from django.db.models import Count
from django.utils import timezone
from rest_framework import serializers
from .models import *


class ReaderSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(read_only=True, many=True, slug_field='book_instances')

    class Meta:
        model = Reader
        fields = "__all__"


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = "__all__"


# class RoomShortSerializer

class BookSerializer(serializers.ModelSerializer):
    readers_limited_instances = serializers.SerializerMethodField()
    book_instances = BookInstanceSerializer(many=True, read_only=True)
    rooms = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ("id", "name", "author", "publisher", "book_instances", "readers_limited_instances", 'rooms')
        read_only_fields = ('id', 'book_instances', 'readers_limited_instances', 'rooms')

    def get_rooms(self, book):
        return Room.objects.filter(book_instances__book=book).values_list('name', flat=True)

    def get_readers_limited_instances(self, book):
        count_book_instance = book.book_instances.count()
        if count_book_instance <= 2:
            readers = Reader.objects.filter(book_taking__book_instance__book=book)
            return ReaderSerializer(readers, many=True).data
        return []


class RoomSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')

    class Meta:
        model = Room
        fields = "__all__"

class BookTakingSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookTaking
        fields = ("book_instance", "reader","data_issue")
#
# class ReadersInfoSerializer(serializers.ModelSerializer):
#     count_lt_20_years = serializers.SerializerMethodField()
#     procent = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Reader
#         field = ('count_lt_20_years', 'procent')
#
#     def get_count_lt_20_years(self, reader):
#         return Reader.objects.filter(birth_date__year__gt=timezone.now().year - 20).count()
#
#
#     def get_procent(self, reader):
#         procent = Reader.objects.all().values('education').annotate(
#             count=Count('id')
#         )
#         print(procent)
#         return {}
